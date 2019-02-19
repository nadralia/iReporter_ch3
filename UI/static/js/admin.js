if(!sessionStorage.token) {
	redirect:window.location.replace('./login.html');
}

const token = sessionStorage.token;

const options = { 
                 method: 'GET', 
				 headers: {
					   'Content-type':'application/json',
						Authorization: `Bearer ${token}`
					} 
				 };
const url = `${rootURL}/incidents`;


const reportSection = document.getElementById('section-reporthistory-wrapper')


let count = 0;
let records = [];
let firstRow, secondRow;
let id, type, createdOn, details,status,images, vidoes, actions;
let idCell, typeCell, createdOnCell, detailsCell, statusCell,imagesCell, vidoesCell,actionsCell;
let idValueCell, typeValueCell, createdOnValueCell, detailsValueCell, statusValueCell,
imagesValueCell, vidoesValueCell,actionsValueCell;

view_incidents();

function view_incidents() {

    fetch(url, options)
    .then(response => response.json())
    .then(data => {
        console.log('successful', data);
		const reportCard = document.createElement('div');
		reportCard.className = 'flex-box-main';
				
		const reportTableDiv = document.createElement('div');
		reportTableDiv.className = 'row-1-of-3';
		reportCard.appendChild(reportTableDiv);

		const table = document.createElement('table');
		table.className = 'table-admin';
		reportTableDiv.appendChild(table);
		
		// create the first rows for the table corresponding 
		// to the record properties
		firstRow = document.createElement('tr');
		firstRow.className = 'row';
		//cells corresponding to first row
		idCell = document.createElement('td');
		idCell.className = 'cell';
		typeCell = document.createElement('td');
		typeCell.className = 'cell';
		createdOnCell= document.createElement('td');
		createdOnCell.className = 'cell';
		detailsCell = document.createElement('td');
		detailsCell.className = 'cell';
		statusCell = document.createElement('td');
		statusCell.className = 'cell';
		
		actionsCell = document.createElement('td');
		actionsCell.className = 'cell';
		
		// I will append the rows to the document fragment,
		// then, when the rows are complete, 
		// append the document fragment to the table
		const documentfragment = new DocumentFragment();
				
		// 1st row: records
		idCell.textContent = 'id'; //id cell
		firstRow.appendChild(idCell);
		idCell.textContent = 'id'; //id cell
		firstRow.appendChild(idCell);
		
		typeCell.textContent = 'type';//type cell
		firstRow.appendChild(typeCell);
		
		createdOnCell.textContent = 'createdOn';//createdOn cell
		firstRow.appendChild(createdOnCell);
		
		detailsCell.textContent = 'comment';//comment cell
		firstRow.appendChild(detailsCell);
		
		statusCell.textContent = 'status';//status cell
		firstRow.appendChild(statusCell);
		
		actionsCell.textContent = 'actions';//actions cell
		firstRow.appendChild(actionsCell);
				
		documentfragment.appendChild(firstRow);
		
        var item_count = data.available_incidents.length;
        if (item_count > 0){
            let row_count = 0;
            for (row_count; row_count<item_count; row_count++) {
                let field_entry = data.available_incidents[row_count];
				//create the row to handle the values
				secondRow = document.createElement('tr');
				secondRow.className = 'row';
				// create the corresponding cell s, to contain the values
				idValueCell = document.createElement('td');
				idValueCell.className = 'cell';
				typeValueCell = document.createElement('td');
				typeValueCell.className = 'cell';
				createdOnValueCell = document.createElement('td');
				createdOnValueCell.className = 'cell';
				detailsValueCell = document.createElement('td');
				detailsValueCell.className = 'cell';
				statusValueCell = document.createElement('td');
				statusValueCell.className = 'cell';
				actionsValueCell = document.createElement('td');
				actionsValueCell.className = 'cell';
				
				 // 2nd row: record type
				idValueCell.textContent = field_entry["incident_id"];
				secondRow.appendChild(idValueCell);
				
				typeValueCell.textContent = field_entry["incident_type"];
				secondRow.appendChild(typeValueCell);
				
				createdOnValueCell.textContent = field_entry["createdon"];
				secondRow.appendChild(createdOnValueCell);
				
				detailsValueCell.textContent = field_entry["comment"];
				secondRow.appendChild(detailsValueCell);
				
				statusValueCell.textContent = field_entry["status"];
				secondRow.appendChild(statusValueCell);
				
				secondRow.appendChild(actionsValueCell);
				
				//delete button
                
				//Edit button
				const btnEdit = document.createElement('button');
                btnEdit.className = 'btn';
                btnEdit.id = 'btn-edit-report';
                btnEdit.textContent = 'Edit Status';
                
				
				// attach the 'buttons' if record status is 'drafted';
                actionsValueCell.appendChild(btnEdit);

				documentfragment.appendChild(secondRow);
				
				// with the rows complete, append the df to the table;
				table.appendChild(documentfragment);
				
				reportSection.appendChild(reportCard);
				
			//add click event 
			// add click event to 'delete button'

				// add click event to 'edit button';
                btnEdit.addEventListener('click', () => {
                       localStorage.recordId = field_entry["incident_id"];
					   redirect:window.location.replace('./edit-status.html');//redirect to edit report page'
                });
				

            }
        }
        else{
            alert("No incidents available");
        }
                
    })
    .catch(function (error) {
        console.log('Request failed', error);
    });
}
