# -*- coding:utf-8 -*-

from django import forms


class ExpressionForm(forms.Form):
    imgFile = forms.FileField(
            label='Select a file',
    )
    # key = forms.CharField(max_length=100)

