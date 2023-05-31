// Wait for the DOM to load
document.addEventListener('DOMContentLoaded', () => {
  // Get the form and input element
  const form = document.getElementById('uploadForm');
  const imageInput = document.getElementById('imageInput');
  const previewContainer = document.getElementById('preview');

  // Listen for form submission
  form.addEventListener('submit', (e) => {
    e.preventDefault();

    // Get the selected image file
    const file = imageInput.files[0];

    // Validate that a file was selected
    if (file) {
      // Create a FormData object to send the file to the server
      const formData = new FormData();
      formData.append('image', file);

      // Send the image file to the server for processing

    //# ...

      fetch('/convert', {
        method: 'POST',
        body: formData
      })
      .then(response => response.blob())
      .then(blob => {
        // Create a URL for the processed image blob
        const imageURL = URL.createObjectURL(blob);

        // Display the converted image
        const image = new Image();
        image.src = imageURL;
        previewContainer.innerHTML = '';
        previewContainer.appendChild(image);

        // Enable print button
        const printButton = document.createElement('button');
        printButton.innerText = 'Print';
        printButton.addEventListener('click', () => {
          window.print();
        });
        previewContainer.appendChild(printButton);
      })
      .catch(error => {
        console.error('An error occurred:', error);
      });
    } else {
      // If no file was selected, display an error message
      console.error('Please select an image file.');
    }
  });
});
