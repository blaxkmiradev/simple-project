from flask import Flask, render_template_string

app = Flask(__name__)

# UI with Flowbite & Tailwind
HTML_CONTENT = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Flask Root App</title>
    <script src="https://cdn.tailwindcss.com"></script>
    <link href="https://cdnjs.cloudflare.com/ajax/libs/flowbite/2.3.0/flowbite.min.css" rel="stylesheet" />
</head>
<body class="bg-white dark:bg-gray-900">
    <nav class="bg-white border-b border-gray-200 px-4 py-2.5 dark:bg-gray-800 dark:border-gray-700">
        <div class="flex flex-wrap justify-between items-center mx-auto max-w-screen-xl">
            <span class="text-xl font-bold dark:text-white">Root Deployment</span>
        </div>
    </nav>
    <section class="py-24">
        <div class="px-4 mx-auto max-w-screen-xl text-center">
            <h1 class="text-4xl font-extrabold text-gray-900 dark:text-white mb-4">Flask is Live</h1>
            <p class="text-gray-500 dark:text-gray-400 mb-8">Hosted in the root directory on Vercel.</p>
            <button class="text-white bg-blue-700 hover:bg-blue-800 font-medium rounded-lg text-sm px-5 py-2.5">Flowbite Component</button>
        </div>
    </section>
    <script src="https://cdnjs.cloudflare.com/ajax/libs/flowbite/2.3.0/flowbite.min.js"></script>
</body>
</html>
"""

@app.route('/')
def home():
    return render_template_string(HTML_CONTENT)

# Essential for Vercel
app.debug = True
