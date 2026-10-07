# Use a pipeline as a high-level helper
from transformers import pipeline

pipe = pipeline("mask-generation", model="facebook/sam3")