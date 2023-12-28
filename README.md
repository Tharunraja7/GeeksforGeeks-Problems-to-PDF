

# 📚 GeeksforGeeks PDF Problem Downloader

This script allows you to download programming problems from GeeksforGeeks as a PDF. You just need to specify the filters on the GeeksforGeeks practice website, copy the URL, and paste it into the script.

## 📥 Installation Steps

1. **🔗 Clone or Download the Repository**: If you have git installed, you can clone the repository using the following command in your terminal:

```bash
git clone https://github.com/Tharunraja7/GeeksforGeeks-Problems-to-PDF.git
```

Alternatively, you can download the repository directly from GitHub by clicking the `Code` button and then `Download ZIP`.

2. **📁 Navigate to the Repository Folder**: Change your current directory to the cloned repository's directory:

```bash
cd GeeksforGeeks-Problems-to-PDF
```

3. **📦 Install Required Packages**: Install the required Python packages using pip:

```bash
pip install -r requirements.txt
```

This command installs all the Python packages listed in the `requirements.txt` file.

## 🚀 Running Steps

1. **🖥️ Run the Script**: You can run the script using the following command:

```bash
python main.py
```

2. **🔗 Enter the URL**: When prompted, paste the URL you copied from the GeeksforGeeks practice website. Go to [https://www.geeksforgeeks.org/explore?page=1](https://www.geeksforgeeks.org/explore?page=1) and apply the filters. Now copy the link. For example: https://www.geeksforgeeks.org/explore?page=1&category=Arrays&company=Amazon&sortBy=submissions. The script will then download the programming problems as a PDF.

## 🌐 Google Colab Usage

You can use Google Colab to run this project in an online Jupyter notebook. Here are two methods to clone the repository in Google Colab:

**Method 1: Using the Open notebook option**
1. Go to [Google Colab](https://colab.research.google.com/).
2. Click on `File` -> `Open notebook`.
3. Select the `GitHub` tab.
4. Enter the URL of the GitHub repository and press Enter.
5. Click on the notebook you want to open.

**Method 2: Using the !git clone command**
1. Go to [Google Colab](https://colab.research.google.com/).
2. Click on `File` -> `New notebook` to create a new notebook.
3. In the first cell of the notebook, clone the repository:

```python
!git clone https://github.com/Tharunraja7/GeeksforGeeks-Problems-to-PDF.git
```

4. Navigate to the cloned repository's directory:

```python
%cd GeeksforGeeks-Problems-to-PDF
```

5. Install the required packages:

```python
!pip install -r requirements.txt
```

6. Run the script in the next cell:

```python
!python main.py
```

To run a cell, click on the play button to the left of the cell.
