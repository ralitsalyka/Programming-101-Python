from django.shortcuts import render, get_object_or_404
from django.views.generic import CreateView
from django.urls import reverse_lazy

from education.models import Lecture


def list(request):
    return render(request, 'lectures/list.html', {'lectures': Lecture.objects.all()})


def detail(request, lecture_id):
    lecture = get_object_or_404(Lecture, id=lecture_id)
    return render(request, 'lectures/detail.html', {'lectures': lecture})


class LectureCreateView(CreateView):
    model = Lecture
    fields = ['name', 'week', 'course', 'url']
    template_name = 'lectures/create.html'

    def get_success_url(self, **kwargs):
        return reverse_lazy('education:lecture:detail', kwargs={'lecture_id': self.object.id})
