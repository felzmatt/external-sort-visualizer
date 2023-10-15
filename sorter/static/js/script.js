function buildTable(N, P, target) {
    const bufferFrames = document.getElementById(target);
    bufferFrames.innerHTML = ''; // Clear previous content
  
    const outerTable = document.createElement('table');
    outerTable.style.borderCollapse = 'collapse'; // Ensure inner tables align correctly

    const pages = Math.ceil(N / P);
    const framesPerRow = 8;
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
            if (target === 'buffer-frames') {
                innerTable.classList.add('buffer-frame');
            } else {
                innerTable.classList.add('relation-page');
            }
            
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

function updateDataRowInAlgorithmDetails(index, phase) {
    const table = document.querySelector('#algorithm-details table');
    const rows = table.rows;
  
    // Check if a data row already exists
    if (rows.length === 2) {
      const dataRow = rows[1];
      const cells = dataRow.cells;
  
      // Update data in the existing cells
      cells[0].innerText = index;
      cells[1].innerText = phase;
    } else {
      // If no data row exists, create a new one
      const newRow = table.insertRow();  // Create a new row
  
      // Create cells and add data to each cell
      const cell1 = newRow.insertCell(0);
      const cell2 = newRow.insertCell(1);
  
      // Populate data in the cells
      cell1.innerText = index;
      cell2.innerText = phase;
    }
  }

function renderStep(relationTables, bufferTables,step) {
    console.log("Rendering step: " + step.index);
    updateDataRowInAlgorithmDetails(step.index, step.phase);
    const relation = step.relation;
    const buffer = step.buffer;
    const tuplesPerBlock = relation[0].length;
    const frames = buffer.length;
    const pages = relation.length;
    // console.log(frames, pages);
    console.log(tuplesPerBlock);
    
    // render buffer frames
    for (let f = 0; f < frames; f++) {
        let bufTuples = bufferTables[f].querySelectorAll('tr');
        //console.log(pageTuples);
        for (let t = 0; t < tuplesPerBlock; t++) {
            // console.log("at position " + f + " "+ t+ " "+ buffer[f][t]);
            let bufTupleAttrs = bufTuples[t].querySelectorAll('td');
            // console.log("at position " + f + " "+ t+ " "+ buffer[f][t]);
            if (buffer[f][t]) {
                bufTupleAttrs[0].innerHTML = buffer[f][t][0];
                bufTupleAttrs[1].innerHTML = buffer[f][t][1];
                bufTupleAttrs[2].innerHTML = buffer[f][t][2];
            } else {
                bufTupleAttrs[0].innerHTML = "-";
                bufTupleAttrs[1].innerHTML = "-";
                bufTupleAttrs[2].innerHTML = "-";
            }
            
        }
    }

    // render relation pages
    for (let p = 0; p < pages; p++) {
        let relTuples = relationTables[p].querySelectorAll('tr');
        // console.log(pageTuples);
        for (let t = 0; t < tuplesPerBlock; t++) {
            // console.log(relation[p][t]);
            let relTupleAttrs = relTuples[t].querySelectorAll('td');
            if (relation[p][t]) {
                relTupleAttrs[0].innerHTML = relation[p][t][0];
                relTupleAttrs[1].innerHTML = relation[p][t][1];
                relTupleAttrs[2].innerHTML = relation[p][t][2];
            } else {
                relTupleAttrs[0].innerHTML = "-";
                relTupleAttrs[1].innerHTML = "-";
                relTupleAttrs[2].innerHTML = "-";
            }
        }
    }

}


  