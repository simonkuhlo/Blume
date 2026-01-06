from django.http import HttpResponse
from django.shortcuts import render, redirect
from Entries.models import EntryV1, CreateCode

def book_start(request) -> HttpResponse:
    context = {"var": "Hallo"}
    return render(request, "book_explorer/book.html", context)

def entry(request, source_id:int) -> HttpResponse:
    pass