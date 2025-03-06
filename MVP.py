{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 3,
   "id": "f7ac5528-318b-473b-84d9-a78829aed5c3",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Collecting openai\n",
      "  Downloading openai-1.65.4-py3-none-any.whl.metadata (27 kB)\n",
      "Requirement already satisfied: streamlit in /opt/anaconda3/lib/python3.12/site-packages (1.37.1)\n",
      "Requirement already satisfied: anyio<5,>=3.5.0 in /opt/anaconda3/lib/python3.12/site-packages (from openai) (4.2.0)\n",
      "Requirement already satisfied: distro<2,>=1.7.0 in /opt/anaconda3/lib/python3.12/site-packages (from openai) (1.9.0)\n",
      "Requirement already satisfied: httpx<1,>=0.23.0 in /opt/anaconda3/lib/python3.12/site-packages (from openai) (0.27.0)\n",
      "Collecting jiter<1,>=0.4.0 (from openai)\n",
      "  Downloading jiter-0.8.2-cp312-cp312-macosx_11_0_arm64.whl.metadata (5.2 kB)\n",
      "Requirement already satisfied: pydantic<3,>=1.9.0 in /opt/anaconda3/lib/python3.12/site-packages (from openai) (2.8.2)\n",
      "Requirement already satisfied: sniffio in /opt/anaconda3/lib/python3.12/site-packages (from openai) (1.3.0)\n",
      "Requirement already satisfied: tqdm>4 in /opt/anaconda3/lib/python3.12/site-packages (from openai) (4.66.5)\n",
      "Requirement already satisfied: typing-extensions<5,>=4.11 in /opt/anaconda3/lib/python3.12/site-packages (from openai) (4.11.0)\n",
      "Requirement already satisfied: altair<6,>=4.0 in /opt/anaconda3/lib/python3.12/site-packages (from streamlit) (5.0.1)\n",
      "Requirement already satisfied: blinker<2,>=1.0.0 in /opt/anaconda3/lib/python3.12/site-packages (from streamlit) (1.6.2)\n",
      "Requirement already satisfied: cachetools<6,>=4.0 in /opt/anaconda3/lib/python3.12/site-packages (from streamlit) (5.3.3)\n",
      "Requirement already satisfied: click<9,>=7.0 in /opt/anaconda3/lib/python3.12/site-packages (from streamlit) (8.1.7)\n",
      "Requirement already satisfied: numpy<3,>=1.20 in /opt/anaconda3/lib/python3.12/site-packages (from streamlit) (1.26.4)\n",
      "Requirement already satisfied: packaging<25,>=20 in /opt/anaconda3/lib/python3.12/site-packages (from streamlit) (24.1)\n",
      "Requirement already satisfied: pandas<3,>=1.3.0 in /opt/anaconda3/lib/python3.12/site-packages (from streamlit) (2.2.2)\n",
      "Requirement already satisfied: pillow<11,>=7.1.0 in /opt/anaconda3/lib/python3.12/site-packages (from streamlit) (10.4.0)\n",
      "Requirement already satisfied: protobuf<6,>=3.20 in /opt/anaconda3/lib/python3.12/site-packages (from streamlit) (4.25.3)\n",
      "Requirement already satisfied: pyarrow>=7.0 in /opt/anaconda3/lib/python3.12/site-packages (from streamlit) (16.1.0)\n",
      "Requirement already satisfied: requests<3,>=2.27 in /opt/anaconda3/lib/python3.12/site-packages (from streamlit) (2.32.3)\n",
      "Requirement already satisfied: rich<14,>=10.14.0 in /opt/anaconda3/lib/python3.12/site-packages (from streamlit) (13.7.1)\n",
      "Requirement already satisfied: tenacity<9,>=8.1.0 in /opt/anaconda3/lib/python3.12/site-packages (from streamlit) (8.2.3)\n",
      "Requirement already satisfied: toml<2,>=0.10.1 in /opt/anaconda3/lib/python3.12/site-packages (from streamlit) (0.10.2)\n",
      "Requirement already satisfied: gitpython!=3.1.19,<4,>=3.0.7 in /opt/anaconda3/lib/python3.12/site-packages (from streamlit) (3.1.43)\n",
      "Requirement already satisfied: pydeck<1,>=0.8.0b4 in /opt/anaconda3/lib/python3.12/site-packages (from streamlit) (0.8.0)\n",
      "Requirement already satisfied: tornado<7,>=6.0.3 in /opt/anaconda3/lib/python3.12/site-packages (from streamlit) (6.4.1)\n",
      "Requirement already satisfied: jinja2 in /opt/anaconda3/lib/python3.12/site-packages (from altair<6,>=4.0->streamlit) (3.1.4)\n",
      "Requirement already satisfied: jsonschema>=3.0 in /opt/anaconda3/lib/python3.12/site-packages (from altair<6,>=4.0->streamlit) (4.23.0)\n",
      "Requirement already satisfied: toolz in /opt/anaconda3/lib/python3.12/site-packages (from altair<6,>=4.0->streamlit) (0.12.0)\n",
      "Requirement already satisfied: idna>=2.8 in /opt/anaconda3/lib/python3.12/site-packages (from anyio<5,>=3.5.0->openai) (3.7)\n",
      "Requirement already satisfied: gitdb<5,>=4.0.1 in /opt/anaconda3/lib/python3.12/site-packages (from gitpython!=3.1.19,<4,>=3.0.7->streamlit) (4.0.7)\n",
      "Requirement already satisfied: certifi in /opt/anaconda3/lib/python3.12/site-packages (from httpx<1,>=0.23.0->openai) (2025.1.31)\n",
      "Requirement already satisfied: httpcore==1.* in /opt/anaconda3/lib/python3.12/site-packages (from httpx<1,>=0.23.0->openai) (1.0.2)\n",
      "Requirement already satisfied: h11<0.15,>=0.13 in /opt/anaconda3/lib/python3.12/site-packages (from httpcore==1.*->httpx<1,>=0.23.0->openai) (0.14.0)\n",
      "Requirement already satisfied: python-dateutil>=2.8.2 in /opt/anaconda3/lib/python3.12/site-packages (from pandas<3,>=1.3.0->streamlit) (2.9.0.post0)\n",
      "Requirement already satisfied: pytz>=2020.1 in /opt/anaconda3/lib/python3.12/site-packages (from pandas<3,>=1.3.0->streamlit) (2024.1)\n",
      "Requirement already satisfied: tzdata>=2022.7 in /opt/anaconda3/lib/python3.12/site-packages (from pandas<3,>=1.3.0->streamlit) (2023.3)\n",
      "Requirement already satisfied: annotated-types>=0.4.0 in /opt/anaconda3/lib/python3.12/site-packages (from pydantic<3,>=1.9.0->openai) (0.6.0)\n",
      "Requirement already satisfied: pydantic-core==2.20.1 in /opt/anaconda3/lib/python3.12/site-packages (from pydantic<3,>=1.9.0->openai) (2.20.1)\n",
      "Requirement already satisfied: charset-normalizer<4,>=2 in /opt/anaconda3/lib/python3.12/site-packages (from requests<3,>=2.27->streamlit) (3.3.2)\n",
      "Requirement already satisfied: urllib3<3,>=1.21.1 in /opt/anaconda3/lib/python3.12/site-packages (from requests<3,>=2.27->streamlit) (2.2.3)\n",
      "Requirement already satisfied: markdown-it-py>=2.2.0 in /opt/anaconda3/lib/python3.12/site-packages (from rich<14,>=10.14.0->streamlit) (2.2.0)\n",
      "Requirement already satisfied: pygments<3.0.0,>=2.13.0 in /opt/anaconda3/lib/python3.12/site-packages (from rich<14,>=10.14.0->streamlit) (2.15.1)\n",
      "Requirement already satisfied: smmap<5,>=3.0.1 in /opt/anaconda3/lib/python3.12/site-packages (from gitdb<5,>=4.0.1->gitpython!=3.1.19,<4,>=3.0.7->streamlit) (4.0.0)\n",
      "Requirement already satisfied: MarkupSafe>=2.0 in /opt/anaconda3/lib/python3.12/site-packages (from jinja2->altair<6,>=4.0->streamlit) (2.1.3)\n",
      "Requirement already satisfied: attrs>=22.2.0 in /opt/anaconda3/lib/python3.12/site-packages (from jsonschema>=3.0->altair<6,>=4.0->streamlit) (23.1.0)\n",
      "Requirement already satisfied: jsonschema-specifications>=2023.03.6 in /opt/anaconda3/lib/python3.12/site-packages (from jsonschema>=3.0->altair<6,>=4.0->streamlit) (2023.7.1)\n",
      "Requirement already satisfied: referencing>=0.28.4 in /opt/anaconda3/lib/python3.12/site-packages (from jsonschema>=3.0->altair<6,>=4.0->streamlit) (0.30.2)\n",
      "Requirement already satisfied: rpds-py>=0.7.1 in /opt/anaconda3/lib/python3.12/site-packages (from jsonschema>=3.0->altair<6,>=4.0->streamlit) (0.10.6)\n",
      "Requirement already satisfied: mdurl~=0.1 in /opt/anaconda3/lib/python3.12/site-packages (from markdown-it-py>=2.2.0->rich<14,>=10.14.0->streamlit) (0.1.0)\n",
      "Requirement already satisfied: six>=1.5 in /opt/anaconda3/lib/python3.12/site-packages (from python-dateutil>=2.8.2->pandas<3,>=1.3.0->streamlit) (1.16.0)\n",
      "Downloading openai-1.65.4-py3-none-any.whl (473 kB)\n",
      "Downloading jiter-0.8.2-cp312-cp312-macosx_11_0_arm64.whl (310 kB)\n",
      "Installing collected packages: jiter, openai\n",
      "Successfully installed jiter-0.8.2 openai-1.65.4\n"
     ]
    }
   ],
   "source": [
    "!pip install openai streamlit"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": None,
   "id": "e920fdf8-6ea3-4f5a-bfe5-b243d939474b",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": 5,
   "id": "32842d0a-646b-4e4d-b466-761a8e7140e3",
   "metadata": {},
   "outputs": [],
   "source": [
    "import openai\n",
    "\n",
    "openai.api_key = \"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\"\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 11,
   "id": "c7066e53-6cf1-4932-9638-ee90d140e89c",
   "metadata": {},
   "outputs": [],
   "source": [
    "import streamlit as st\n",
    "\n",
    "def generate_gift_ideas(occasion, recipient, budget, relationship):\n",
    "    prompt = f\"\"\"\n",
    "    Suggest 5 unique and thoughtful gift ideas for a {relationship} who is {recipient} years old.\n",
    "    The occasion is {occasion}, and the budget is {budget}.\n",
    "    Provide a short description for each gift idea.\n",
    "    \"\"\"\n",
    "    \n",
    "    response = openai.ChatCompletion.create(\n",
    "        model=\"gpt-4\",\n",
    "        messages=[{\"role\": \"user\", \"content\": prompt}]\n",
    "    )\n",
    "    \n",
    "    return response[\"choices\"][0][\"message\"][\"content\"]\n",
    "\n",
    "# Streamlit UI\n",
    "st.title(\"🎁 AI Gift Recommender\")\n",
    "\n",
    "occasion = st.selectbox(\"Select Occasion\", [\"Birthday\", \"Anniversary\", \"Graduation\", \"Wedding\", \"Housewarming\", \"Valentine's Day\"])\n",
    "recipient_age = st.number_input(\"Recipient's Age\", min_value=1, max_value=100, value=25)\n",
    "relationship = st.selectbox(\"Relationship\", [\"Friend\", \"Partner\", \"Parent\", \"Sibling\", \"Colleague\"])\n",
    "budget = st.selectbox(\"Select Budget\", [\"Under ₹500\", \"₹500 - ₹2000\", \"₹2000 - ₹5000\", \"Above ₹5000\"])\n",
    "\n",
    "if st.button(\"Get Gift Ideas\"):\n",
    "    st.write(\"**AI Suggestions:**\")\n",
    "    gift_ideas = generate_gift_ideas(occasion, recipient_age, budget, relationship)\n",
    "    st.write(gift_ideas)\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": None,
   "id": "235f2e71-48b9-428b-bab7-af43497e2ab2",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python [conda env:base] *",
   "language": "python",
   "name": "conda-base-py"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.12.7"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
