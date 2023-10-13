function loadFile() {
    const fileInput = document.getElementById('fileInput');
    
    // Ensure a file was selected
    if (fileInput.files.length === 0) {
      alert('Please select a file.');
      return;
    }
  
    const file = fileInput.files[0];
    const reader = new FileReader();
  
    // Define a callback to handle the file reading
    reader.onload = function(event) {
      const fileContent = event.target.result;
      
      try {
        const jsonData = JSON.parse(fileContent);
        console.log('Parsed JSON data:', jsonData);
        // Do something with the parsed JSON data
      } catch (error) {
        console.error('Error parsing JSON:', error);
      }
    };
  
    // Read the file as text
    reader.readAsText(file);
  }
  