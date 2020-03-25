from django import forms

#スレッド作成用のフォーム
class CreatethreadForm(forms.Form):
   threadname = forms.CharField(max_length=100,label='スレッド名')
   name = forms.CharField(max_length=100,label='名前')

#掲示板に投稿する用のフォーム
class ThreadContentForm(forms.Form):
   name = forms.CharField(max_length=100,label='名前')
   content = forms.CharField(widget=forms.Textarea,label='投稿内容')

#削除依頼用
class DeleteRequestForm(forms.Form):
   delete_threadid = forms.IntegerField(label='スレッドID')
   reason_delete = forms.CharField(widget=forms.Textarea,label='削除依頼理由')

#管理者ログインページ
class ManagerLoginForm(forms.Form):
   managerusername = forms.CharField(label='ユーザー名')
   password = forms.CharField(label='パスワード')