function buildTable(N, P) {
    const bufferFrames = document.getElementById('buffer-frames');
    bufferFrames.innerHTML = ''; // Clear previous content
  
    const outerTable = document.createElement('table');
    outerTable.style.borderCollapse = 'collapse'; // Ensure inner tables align correctly

    const pages = Math.ceil(N / P);
    const framesPerRow = 10;
    const numOuterRows = Math.ceil(pages / framesPerRow);
    const innerTables = []; // Array to store references to inner tables

    let currentIndex = 0;
    let tuples = 0;
  
    for (let i = 0; i < numOuterRows; i++) {
        if (currentIndex >= pages) break;
        const outerRow = outerTable.insertRow();
  
        for (let j = 0; j < framesPerRow; j++) {
            if (currentIndex >= pages) break;
  
            const innerTable = document.createElement('table');
            innerTable.classList.add('buffer-frame');
            innerTable.style.border = '1px solid black'; // Border for demonstration
  
            for (let k = 0; k < P; k++) {
                const row = innerTable.insertRow();
                const cell1 = row.insertCell(0);
                const cell2 = row.insertCell(1);
                const cell3 = row.insertCell(2);
                if (tuples >= N) {
                    cell1.innerText = "-";
                    cell2.innerText = "-";
                    cell3.innerText = "-"; // Random age for demonstration
                } else {
                    cell1.innerText = tuples;
                    cell2.innerText = `Name${currentIndex}`;
                    cell3.innerText = Math.floor(Math.random() * 100); // Random age for demonstration
                    tuples++;
                }
            }
  
            const outerCell = outerRow.insertCell();
            outerCell.appendChild(innerTable);
            innerTables.push(innerTable); // Store reference to the inner table
            currentIndex++;
        }
    }
  
    bufferFrames.appendChild(outerTable);

    // Return the array of inner tables for easy access later
    return innerTables;
}

function renderAlgorithmStep(tape, step_index) {
    step = tape[index];
    
}
function highlightFirstTuple(innerTables, pageIndex) {
    // Ensure the provided page index is valid
    if (pageIndex >= 0 && pageIndex < innerTables.length) {
      const tableRows = innerTables[pageIndex].querySelectorAll('tr');
  
      // Apply green color to the first row
      if (tableRows.length > 0) {
        tableRows[0].classList.add('highlighted-row');
      }
    } else {
      console.error('Invalid page index.');
    }
}
  