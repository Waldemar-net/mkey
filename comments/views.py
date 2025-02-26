from importlib.metadata import requires
from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required
from django.urls import reverse
from goods.models import Products
from comments.models import Comments
from comments.forms import CommentForm  # assuming you have a form defined in forms.py

@login_required
def add_comment(request, product_id):
    product = Products.objects.get(id=product_id)
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.user = request.user
            comment.product = product
            comment.save()
            
        return redirect(reverse('goods:product', args=[product.slug]))
    else:
        form = CommentForm()
    return render(request, 'add_comment.html', {'form': form, 'product': product})