import os
import sys
import pdfx
import nltk
import json
import spacy
import random
import requests
import numpy as np
import pandas as pd
from nltk import pos_tag
from zipfile import ZipFile
from bs4 import BeautifulSoup
from pymongo import MongoClient
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.stem import WordNetLemmatizer
from src.exception import CustomException
from flask import send_from_directory, redirect, url_for
from sklearn.metrics.pairwise import cosine_similarity
from src.components.data_transformation import Preprocessing
from flask import Flask,request,render_template,Response,send_file,redirect,session
from transformers import AutoTokenizer, AutoModelForSequenceClassification
from sklearn.feature_extraction.text import TfidfVectorizer, CountVectorizer
from src.pipeline.predict_pipeline import CustomData,PreprocessPipeline,ModelPipeline,WebScraping,Recommend

