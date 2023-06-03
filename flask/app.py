from flask import Flask, render_template, request, send_file
import cv2
import numpy as np
import io
from flask_cors import CORS

app = Flask(__name__)
CORS(app)
app.config['WTF_CSRF_ENABLED'] = False

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/convert', methods=['POST'])
def convert():
    if request.method == 'POST':
        # Get the uploaded image file
        file = request.files['image']

        # Read the image using OpenCV
        image = cv2.imdecode(np.fromstring(file.read(), np.uint8), cv2.IMREAD_COLOR)

        # Perform image processing and conversion
        # ... Implement your own logic here ...
        # Convert the image to black and white outline
        gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        _, threshold = cv2.threshold(gray, 127, 255, cv2.THRESH_BINARY_INV)

        # Create a byte buffer to store the converted image
        buffer = io.BytesIO()

        # Save the converted image to the buffer in PNG format
        cv2.imwrite(buffer, threshold, format='PNG')

        # Set the buffer position to the start
        buffer.seek(0)

        # Return the converted image as a response
        return send_file(buffer, mimetype='image/png')

    # If the request method is not POST, return an error
    return "Method Not Allowed", 405

if __name__ == '__main__':
    app.run(debug=True)


# from flask import Flask, render_template, request, send_file
# import cv2
# import numpy as np
# import io
# from nltk.tokenize import sent_tokenize
# from sklearn.feature_extraction.text import CountVectorizer
# from sklearn.metrics.pairwise import cosine_similarity
# from flask_cors import CORS

# app = Flask(__name__)
# CORS(app)

# app.config['WTF_CSRF_ENABLED'] = False

# @app.route('/')
# def index():
#     return render_template('index.html')

# @app.route('/convert', methods=['POST'])
# def convert():
#     # Get the uploaded image file
#     file = request.files['image']

#     # Read the image using OpenCV
#     image = cv2.imdecode(np.fromstring(file.read(), np.uint8), cv2.IMREAD_COLOR)

#     # Perform image processing and conversion
#     # ... Implement your own logic here ...
#     # Convert the image to black and white outline
#     gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
#     _, threshold = cv2.threshold(gray, 127, 255, cv2.THRESH_BINARY_INV)

#     # Create a byte buffer to store the converted image
#     buffer = io.BytesIO()

#     # Save the converted image to the buffer in PNG format
#     cv2.imwrite(buffer, threshold, format='PNG')

#     # Set the buffer position to the start
#     buffer.seek(0)

#     # Return the converted image as a response
#     return send_file(buffer, mimetype='image/png')

# if __name__ == '__main__':
#     app.run(debug=True)
#
# from nltk.tokenize import sent_tokenize
# from sklearn.feature_extraction.text import CountVectorizer
# from sklearn.metrics.pairwise import cosine_similarity
#
#
# def extractive_summarize(text, num_sentences):
#     # Split the text into sentences
#     sentences = sent_tokenize(text)
#
#     # Create a bag-of-words representation of the sentences
#     vectorizer = CountVectorizer().fit_transform(sentences)
#
#     # Calculate the cosine similarity between sentences
#     similarity_matrix = cosine_similarity(vectorizer)
#
#     from flask import Flask, render_template, request, send_file
#     import cv2
#     import numpy as np
#     import io
#
#     app = Flask(__name__)
#
#     @app.route('/')
#     def index():
#         return render_template('index.html')
#
#     @app.route('/convert', methods=['POST'])
#     def convert():
#         # Get the uploaded image file
#         file = request.files['image']
#
#         # Read the image using OpenCV
#         image = cv2.imdecode(np.fromstring(file.read(), np.uint8), cv2.IMREAD_COLOR)
#
#         # Perform image processing and conversion
#         # ... Implement your own logic here ...
#         # Convert the image to black and white outline
#         gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
#         _, threshold = cv2.threshold(gray, 127, 255, cv2.THRESH_BINARY_INV)
#
#         # Create a byte buffer to store the converted image
#         buffer = io.BytesIO()
#
#         # Save the converted image to the buffer in PNG format
#         cv2.imwrite(buffer, converted_image, format='PNG')
#
#         # Set the buffer position to the start
#         buffer.seek(0)
#
#         # Return the converted image as a response
#         return send_file(buffer, mimetype='image/png')
#
#     if __name__ == '__main__':
#         app.run(debug=True)

    # Get the top n sentences with the highest similarity