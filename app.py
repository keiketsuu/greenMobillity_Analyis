import streamlit as st
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from scipy.stats import pointbiserialr

# Load dataset
dataset = pd.read_excel('D:\Downloads\ML\Datasets\greenMobility\greenMobility.xlsx')

# Title
st.title('Green Mobility Survey Dashboard')

# Section 1: Age Distribution Pie Chart and Transport Mode Pie Chart
st.header('👥 Age Distribution and 🚗 Transport Mode Distribution')

# Age Distribution Pie Chart
age_counts = dataset['What is your age category?  '].value_counts()
fig_age = plt.figure(figsize=(3, 3))
plt.pie(age_counts, labels=age_counts.index, autopct='%0.0f%%', startangle=90, colors=plt.cm.Paired.colors, textprops={'fontsize': 5})
plt.title('Age Distribution')
st.pyplot(fig_age)

# Transport Mode Pie Chart
transport_counts = dataset['What is your primary mode of transportation for commuting to work or school?'].value_counts()
fig_transport = plt.figure(figsize=(15, 15))
sns.set_palette("pastel")
plt.pie(transport_counts, labels=transport_counts.index, autopct='%1.1f%%', startangle=50, counterclock=False)
plt.title('Distribution of Principal Means of Transport')
st.pyplot(fig_transport)

# Section 2: Knowledge about Eco-Friendly Transport Options Bar Plot and Time Spent on Daily Commute Histogram
st.header('♻️ Eco-Friendly Knowledge Distribution and 🕒 Time Spent on Daily Commute Histogram')

# Knowledge about Eco-Friendly Transport Options Bar Plot
response_counts = dataset['Are you aware of eco-friendly transportation options available in your area?  '].value_counts()
fig_response = plt.figure(figsize=(15, 15))
sns.set_palette("pastel")
sns.barplot(x=response_counts.index, y=response_counts.values, palette=['red', 'green'])
plt.title('Distribution of Knowledge about Eco-Friendly Transport Options')
plt.xlabel('Response')
plt.ylabel('Count')
total_responses = len(dataset)
for i, count in enumerate(response_counts):
    plt.text(i, count + 0.1, f'{count / total_responses * 100:.1f}%', ha='center', va='bottom')
st.pyplot(fig_response)

# Time Spent on Daily Commute Histogram
filtered_dataset = dataset[dataset['On average, how much time you spend on your daily commute?'] != '30 - 60 , 1h +']
fig_commute_time = plt.figure(figsize=(10, 6))
sns.histplot(filtered_dataset, x="On average, how much time you spend on your daily commute?")
plt.xticks(rotation=45, fontsize=12)
st.pyplot(fig_commute_time)
