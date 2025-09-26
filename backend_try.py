import base64
import os
import time
import requests
from fastapi import FastAPI, Form, File, UploadFile
#read
from fastapi.middleware.cors import CORSMiddleware
#read
from fastapi.responses import JSONResponse
import uvicorn
from typing import List
import random
from prompts import PROMPTS

def sample_prompts(mode: str, count: int | None = None):
    """Return up to `count` prompts for a mode (all if count is None).
    Safeguards against IndexError if prompt lists are shortened.
    """

    plist=PROMPTS.get(mode,[]) or []
    if count is None or count >= len(plist):
        return plist
    return plist[:count]


