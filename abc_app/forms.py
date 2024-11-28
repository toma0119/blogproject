from django.forms import ModelForm
from .models import PhotoPost
from django import forms

class PhotoPostForm(ModelForm):
    class Meta:
        model = PhotoPost
        fields = ['category', 'title', 'comment', 'image1', 'image2']

class ContactForm(forms.Form):
    # フォームのフィールドをクラス変数として定義
    name = forms.CharField(label='お名前')
    email = forms.EmailField(label='メールアドレス')
    title = forms.CharField(label='件名')
    message = forms.CharField(label='メッセージ',widget=forms.Textarea)
    
    def __init__ (self,*args,**kwargs):
        '''ContactFormのコンストラクター
        
        フィールドの初期化を行う
        '''
        super().__init__(*args,**kwargs)
        #nameフィールドのplaceholderにメッセージを登録
        self.fields['name'].widget.attrs['placeholder'] = \
            'お名前を入力してください'
        # nameフィールドを出力する<input>タグのclass属性を設定
        self.fields['name'].widget.attrs['class'] = 'form-control'
        
        self.fields['email'].widget.attrs['placeholder'] = \
            'メールアドレスを入力してください'
        self.fields['email'].widget.attrs['class'] = 'form-control'
        
        #titleフィールドのplaceholderにメッセージを登録
        self.fields['title'].widget.attrs['placeholder'] = \
            'タイトルを入力してください'
        # titleフィールドを出力する<input>タグのclass属性を設定
        self.fields['title'].widget.attrs['class'] = 'form-control'
        
        # messageフィールドのplaceholderにメッセージを登録
        self.fields['message'].widget.attrs['placeholder'] = \
            'メッセージを入力してください'
        # messageフィールドを出力する<input>タグのclass属性を設定
        self.fields['message'].widget.attrs['class'] = 'form-control'