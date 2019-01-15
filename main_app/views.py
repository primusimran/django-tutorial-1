from django.http import HttpResponse
def homeView(request):
	return HttpResponse('<h1>Alhamdulillah</h1>')