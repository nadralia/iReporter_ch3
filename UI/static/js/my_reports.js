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
const reportHistory = document.createElement('div');
reportHistory.className = 'flex-box-reporthistory';

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
		reportTableDiv.className = 'table-table-row-div';
		reportCard.appendChild(reportTableDiv);

		const table = document.createElement('table');
		table.className = 'report-history-table';
		reportTableDiv.appendChild(table);
		
		// create the first rows for the table corresponding 
		// to the record properties
		firstRow = document.createElement('tr');
		firstRow.className = 'table-row';
		//cells corresponding to first row
		idCell = document.createElement('td');
		idCell.className = 'table-cell';
		typeCell = document.createElement('td');
		typeCell.className = 'table-cell';
		createdOnCell= document.createElement('td');
		createdOnCell.className = 'table-cell';
		detailsCell = document.createElement('td');
		detailsCell.className = 'table-cell';
		statusCell = document.createElement('td');
		statusCell.className = 'table-cell';
		
		actionsCell = document.createElement('td');
		actionsCell.className = 'table-cell';
		
		// I will append the rows to the document fragment,
		// then, when the rows are complete, 
		// append the document fragment to the table
		const documentfragment = new DocumentFragment();
				
		// 1st row: records
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
				secondRow.className = 'table-row';
				// create the corresponding cell s, to contain the values
				idValueCell = document.createElement('td');
				idValueCell.className = 'table-cell';
				typeValueCell = document.createElement('td');
				typeValueCell.className = 'table-cell';
				createdOnValueCell = document.createElement('td');
				createdOnValueCell.className = 'table-cell';
				detailsValueCell = document.createElement('td');
				detailsValueCell.className = 'table-cell';
				statusValueCell = document.createElement('td');
				statusValueCell.className = 'table-cell';
				actionsValueCell = document.createElement('td');
				actionsValueCell.className = 'table-cell';
				
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
				const btnDelete = document.createElement('button');
                btnDelete.className = 'btn';
                btnDelete.id = 'btn-delete-report';
                btnDelete.textContent = 'Delete';
                
				//Edit button
				const btnEdit = document.createElement('button');
                btnEdit.className = 'btn';
                btnEdit.id = 'btn-edit-report';
                btnEdit.textContent = 'Edit';
                
				
				// attach the 'buttons' if record status is 'drafted';
                if (field_entry["status"] === 'drafted') {
                    actionsValueCell.appendChild(btnDelete);
                    actionsValueCell.appendChild(btnEdit);
                }
				
				const btnView = document.createElement('button');
                btnView.className = 'btn';
                btnView.id = 'btn-view-report';
                btnView.textContent = 'View';
                actionsValueCell.appendChild(btnView);
				

				documentfragment.appendChild(secondRow);
				
				// with the rows complete, append the df to the table;
				table.appendChild(documentfragment);
				
				reportHistory.appendChild(reportCard);
				
				
			//add click event 
			// add click event to 'delete button'
                btnDelete.addEventListener('click', async (event) => {
					let x = confirm("Are you sure you want to delete this report?");
					if (x){
					   try {
						  const delete_report = await deleteReport(field_entry["incident_id"]);
						} catch(err) {
							console.log(err);
						};
					}
					else{
						return false;
					}
					   
				});
				// add click event to 'edit button';
                btnEdit.addEventListener('click', () => {
                       localStorage.recordId = field_entry["incident_id"];
                       localStorage.recordType =field_entry["incident_type"];
                       localStorage.recordLatitude = field_entry["latitude"];
					   localStorage.recordLongitude = field_entry["longitude"];
                       localStorage.recordComment = field_entry["comment"];
                       localStorage.recordImages = field_entry["images"];
                       localStorage.recordVideos = field_entry["videos"];
					   redirect:window.location.replace('./edit-report.html');//redirect to edit report page'
                });
				
				// add click event to 'edit button';
                btnView.addEventListener('click', () => {
                       localStorage.recordId = field_entry["incident_id"];
                       localStorage.recordType =field_entry["incident_type"];
                       localStorage.recordLatitude = field_entry["latitude"];
					   localStorage.recordLongitude = field_entry["longitude"];
                       localStorage.recordComment = field_entry["comment"];
                       localStorage.recordImages = field_entry["images"];
                       localStorage.recordVideos = field_entry["videos"];
					   redirect:window.location.replace('./view-report.html');//redirect to view report page
                });
				
				reportSection.appendChild(reportHistory);

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



let deleteReport = async (incident_id) => {
	
    const del_url = `${rootURL}/incidents/${incident_id}`;
    const options = { 
	                 method: 'DELETE', 
					 mode: 'cors', 
					 headers: {
					   'Content-type':'application/json',
						Authorization: `Bearer ${token}`
					} 
					};

    const request = new Request(del_url, options);

    try {
        const response = await fetch(request);
        const jsonData = await response.json();
        if(jsonData.status === 200) {
            
        } else {
            console.log(jsonData)
			redirect:window.location.reload();
        }
    } catch (err) {
        console.log(err);
    }
};