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

const redflags_url = `${rootURL}/red-flags`;
const interventions_url = `${rootURL}/interventions`;

const redflagsFetch = fetch(redflags_url, options);
const interventionsFetch = fetch(interventions_url, options);

Promise.all([redflagsFetch, interventionsFetch])
.then((responseArr) => {
    responseArr.forEach(response => {
        getResponse(response.json()); // the .json() method returns a promise
    });
}).catch(err => {
    console.log(err);
});

//my_report section report-history-section
//div report-history-section-content
//div       

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

const getResponse = (responseJson) => {
    responseJson.then((responseObj) => {
		
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
		
		count += 1;
        records = records.concat(responseObj.data); // merge new array with the existing one.

       if(count > 1) { // i. if process() function has been called twice, since we are making two requests
           if (records.length > 0) {
               records.sort((a, b) => a.id - b.id);
               records.forEach(record => {
				   
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
				idValueCell.textContent = record.incident_id;
				secondRow.appendChild(idValueCell);
				
				typeValueCell.textContent = record.incident_type;
				secondRow.appendChild(typeValueCell);
				
				createdOnValueCell.textContent = record.createdon;
				secondRow.appendChild(createdOnValueCell);
				
				detailsValueCell.textContent = record.comment;
				secondRow.appendChild(detailsValueCell);
				
				statusValueCell.textContent = record.status;
				secondRow.appendChild(statusValueCell);
				
				secondRow.appendChild(actionsValueCell);
				
				//delete button
				const btnDelete = document.createElement('button');
                btnDelete.className = 'btn';
                btnDelete.id = 'btn-edit-report';
                btnDelete.textContent = 'Delete';
                
				//Edit button
				const btnEdit = document.createElement('button');
                btnEdit.className = 'btn';
                btnEdit.id = 'btn-edit-report';
                btnEdit.textContent = 'Edit';
                
				
				// attach the 'buttons' if record status is 'drafted';
                if (record.status === 'drafted') {
                    actionsValueCell.appendChild(btnDelete);
                    actionsValueCell.appendChild(btnEdit);
                }
				
				const btnView = document.createElement('button');
                btnView.className = 'btn';
                btnView.id = 'btn-edit-report';
                btnView.textContent = 'View';
                actionsValueCell.appendChild(btnView);
				

				documentfragment.appendChild(secondRow);
				
				// with the rows complete, append the df to the table;
				table.appendChild(documentfragment);
				
				reportHistory.appendChild(reportCard);
				
				// add click event to 'edit button';
                btnEdit.addEventListener('click', () => {
                       localStorage.recordId = record.incident_id;
                       localStorage.recordType = record.incident_type;
                       localStorage.recordLatitude = record.latitude;
					   localStorage.recordLongitude = record.longitude;
                       localStorage.recordComment = record.comment;
                       localStorage.recordImages = record.images;
                       localStorage.recordVideos = record.videos;
					   redirect:window.location.replace('./edit-report.html');//redirect to edit report page'
                });
				
				// add click event to 'edit button';
                btnView.addEventListener('click', () => {
                       localStorage.recordId = record.incident_id;
                       localStorage.recordType = record.incident_type;
                       localStorage.recordLatitude = record.latitude;
					   localStorage.recordLongitude = record.longitude;
                       localStorage.recordComment = record.comment;
                       localStorage.recordImages = record.images;
                       localStorage.recordVideos = record.videos;
					   redirect:window.location.replace('./view-report.html');//redirect to view report page
                });
				   
			   });
			   reportSection.appendChild(reportHistory);
		   }
	   }
		
    });
};