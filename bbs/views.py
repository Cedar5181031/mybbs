from datetime import datetime

from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.db.models import Max
from django.shortcuts import render, redirect

from bbs.forms import CreatethreadForm,ThreadContentForm, DeleteRequestForm,ManagerLoginForm
from bbs.models import Threaddb, threadcontentdb, thread_deleterequestdb, manager_userdb, threadcontent_deleterequestdb


#スレッド一覧表示(ホーム画面)
def threadlist(request):

    #データの取得
    all_data = Threaddb.objects.all().order_by('id')

    #ページネーション機能(ページ分け機能)
    page = Paginator(all_data, 10)
    pagenum = request.GET.get('pagenum')

    params = {
        'id':'ID',
        'threadname':'スレッド名',
        'threadcreater':'スレッド作成者',
        'data': page.get_page(pagenum),
    }
    return render(request, 'bbs/threadlist.html', params)

#スレッド作成画面
def createthread(request):
    params = {
        'form': CreatethreadForm(),
    }
    if(request.method == 'POST'):
        name = request.POST['name']
        threadname = request.POST['threadname']
        Thread = Threaddb(name=name, threadname=threadname)
        Thread.save()
        return redirect(to='threadlist')
    return render(request, 'bbs/createthread.html', params)

#スレッド内部
def threadcontent(request,id):

    #データの取得
    titledata = Threaddb.objects.filter(id=id)
    all_data = threadcontentdb.objects.filter(threadid=titledata.values().get()['id']).all().order_by('id')

    #スレッドごとにidを連番にするためにスレッドにある最大idを取得
    count = threadcontentdb.objects.filter(threadid=titledata.values().get()['id']).aggregate(Max('count'))
    max = count["count__max"]

    #ページネーション機能(ページ分け機能)
    page = Paginator(all_data,50)
    pagenum = request.GET.get('pagenum')

    params = {
        'id':id,
        'form': ThreadContentForm(),
        'data': page.get_page(pagenum),
        'threadtitle': titledata.values().get()['threadname']
    }

    if(request.method == 'POST'):
        f_threadid=Threaddb.objects.get(id=id)
        sf_threadid=f_threadid
        name = request.POST['name']
        content = request.POST['content']

        #初回時に数値が入っていないとき、1を代入する
        if not max is None:
            count=int(max)+1
        else:
            count=1
        ThreadContent = threadcontentdb(name=name,content=content,threadid=sf_threadid,count=count)
        ThreadContent.save()
        return redirect(request.META['HTTP_REFERER'])
    return render(request,'bbs/threadcontent.html',params)

#スレッド削除依頼ページ
def thread_deleterequest(request):
    params = {
        'form':DeleteRequestForm(),
    }
    if(request.method == 'POST'):
        delete_threadid = request.POST['delete_threadid']
        reason_delete = request.POST['reason_delete']
        deleterequest = thread_deleterequestdb(delete_threadid=delete_threadid,reason_delete=reason_delete)
        deleterequest.save()
        return redirect(to='threadlist')
    return render(request,'bbs/delete_request.html',params)

#投稿削除依頼ページ
def threadcontentrequest(request):
    params = {
        'form': DeleteRequestForm(),
    }
    if(request.method== 'POST'):
        delete_contentid = request.POST['delete_threadid']
        reason_delete = request.POST['reason_delete']
        deleterequest = threadcontent_deleterequestdb(delete_contentid=delete_contentid,reason_delete=reason_delete)
        deleterequest.save()
        return redirect(to='/bbs/threadcontent/'+request.session.get('threadid'))
    request.session['threadid'] = request.GET.get('p')
    return render(request,'bbs/threadcontent_delrequest.html',params)

#管理者ログインページ
def manager_login(request):
    params = {
        'form':ManagerLoginForm(),
    }
    if(request.method == 'POST'):
        username = request.POST['managerusername']
        password = request.POST['password']
        judge = manager_userdb.objects.filter(username=username,password=password)
        if not judge:
            return redirect(to='manager_login')
        else:
            return redirect(to='manager_page')
    return render(request,'bbs/manager_login.html',params)

#管理者ページ
def manager_page(request):
    return render(request,'bbs/manager_page.html')
# Create your views here.

