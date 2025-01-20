let subjects = [];
const MAX_SUBJECTS = 5;
let timetableData = {}; // Store the timetable data
let attendanceData = {}; // Store attendance data for each subject
let currentMonth = new Date().getMonth(); // Track the current month
let currentYear = new Date().getFullYear(); // Track the current year

document.getElementById('addSubject').addEventListener('click', addSubject);
document.getElementById('closePopup').addEventListener('click', () => {
    document.getElementById('attendancePopup').classList.add('hidden');
});
document.getElementById('setTimetable').addEventListener('click', showSetTimetablePopup);
document.getElementById('closeSetTimetablePopup').addEventListener('click', () => {
    document.getElementById('setTimetablePopup').classList.add('hidden');
});
document.getElementById('confirmTimetable').addEventListener('click', confirmTimetable);

function addSubject() {
    if (subjects.length >= MAX_SUBJECTS) {
        alert("You have reached the maximum number of subjects.");
        return;
    }

    const subjectName = prompt("Enter subject name:");
    if (subjectName) {
        subjects.push(subjectName);
        const timetable = document.getElementById('timetable');
        const subjectDiv = document.createElement('div');
        subjectDiv.textContent = subjectName;
        subjectDiv.className = 'subject';
        subjectDiv.addEventListener('click', () => showAttendance(subjectName));
        timetable.appendChild (subjectDiv);

        if (subjects.length === MAX_SUBJECTS) {
            document.getElementById('setTimetable').classList.remove('hidden');
            alert("You have added all subjects. Now set the timetable.");
        }
    } else {
        alert("Subject name cannot be empty.");
    }
}

function showAttendance(subject) {
    const attendanceDetails = document.getElementById('attendanceDetails');
    attendanceDetails.textContent = `Attendance for ${subject}: 10/15 (66.67%)`; // Example data

    // Display the calendar for attendance
    displayCalendar(subject, currentMonth, currentYear);

    document.getElementById('attendancePopup').classList.remove('hidden');
}

function displayCalendar(subject, month, year) {
    const calendar = document.getElementById('calendar');
    calendar.innerHTML = ''; // Clear previous calendar

    const daysInMonth = new Date(year, month + 1, 0).getDate();
    const currentMonthName = new Date(year, month).toLocaleString('default', { month: 'long' });

    const monthHeader = document.createElement('h3');
    monthHeader.textContent = `${currentMonthName} ${year}`;
    calendar.appendChild(monthHeader);

    // Create navigation buttons
    const navContainer = document.createElement('div');
    const prevButton = document.createElement('button');
    prevButton.textContent = 'Previous';
    prevButton.addEventListener('click', () => {
        currentMonth = (currentMonth === 0) ? 11 : currentMonth - 1; // Go to previous month
        if (currentMonth === 11) currentYear--; // Decrease year if going from January to December
        displayCalendar(subject, currentMonth, currentYear);
    });

    const nextButton = document.createElement('button');
    nextButton.textContent = 'Next';
    nextButton.addEventListener('click', () => {
        currentMonth = (currentMonth === 11) ? 0 : currentMonth + 1; // Go to next month
        if (currentMonth === 0) currentYear++; // Increase year if going from December to January
        displayCalendar(subject, currentMonth, currentYear);
    });

    navContainer.appendChild(prevButton);
    navContainer.appendChild(nextButton);
    calendar.appendChild(navContainer);

    const daysContainer = document.createElement('div');
    daysContainer.className = 'days-container';

    for (let day = 1; day <= daysInMonth; day++) {
        const dayDiv = document.createElement('div');
        dayDiv.className = 'day';
        dayDiv.textContent = day;

        // Check if attendance is marked for the day
        if (attendanceData[`${subject}-${day}`]) {
            dayDiv.classList.add('present'); // Add a class for present days
        }

        // Add attendance marking functionality
        dayDiv.addEventListener('click', () => markAttendance(subject, day));
        daysContainer.appendChild(dayDiv);
    }

    calendar.appendChild(daysContainer);
}

function markAttendance(subject, day) {
    const attendanceKey = `${subject}-${day}`;
    if (!attendanceData[attendanceKey]) {
        attendanceData[attendanceKey] = true; // Mark attendance as present
        alert(`Attendance marked for ${subject} on day ${day}`);
    } else {
        delete attendanceData[attendanceKey]; // Unmark attendance
        alert(`Attendance unmarked for ${subject} on day ${day}`);
    }
    displayCalendar(subject, currentMonth, currentYear); // Refresh calendar to show updated attendance
}

function showSetTimetablePopup() {
    const subjectTimeInputs = document.getElementById('subjectTimeInputs');
    subjectTimeInputs.innerHTML = ''; // Clear previous inputs

    subjects.forEach(subject => {
        const inputDiv = document.createElement('div');
        inputDiv.innerHTML = `
            <label>${subject} - Days:</label><br>
            <input type="checkbox" id="${subject}-Monday"> Monday<br>
            <input type="checkbox" id="${subject}-Tuesday"> Tuesday<br>
            <input type="checkbox" id="${subject}-Wednesday"> Wednesday<br>
            <input type="checkbox" id="${subject}-Thursday"> Thursday<br>
            <input type="checkbox" id="${subject}-Friday"> Friday<br>
            <label>Time:</label>
            <input type="time" id="${subject}-time" required>
        `;
        subjectTimeInputs.appendChild(inputDiv);
    });

    document.getElementById('setTimetablePopup').classList.remove('hidden');
}



function confirmTimetable() {
    timetableData = {}; // Reset timetable data
    let allValid = true; // Flag to check if all subjects are valid

    subjects.forEach(subject => {
        const days = [];
        if (document.getElementById(`${subject}-Monday`).checked) days.push("Monday");
        if (document.getElementById(`${subject}-Tuesday`).checked) days.push("Tuesday");
        if (document.getElementById(`${subject}-Wednesday`).checked) days.push("Wednesday");
        if (document.getElementById(`${subject}-Thursday`).checked) days.push("Thursday");
        if (document.getElementById(`${subject}-Friday`).checked) days.push("Friday");
        
        const time = document.getElementById(`${subject}-time`).value;
        if (days.length > 0 && time) { // Ensure at least one day is selected and time is provided
            timetableData[subject] = { days, time };
        } else {
            alert(`Please set days and time for ${subject}.`);
            allValid = false; // Mark as invalid
        }
    });

    if (allValid) {
        displayTimetable(); // Call function to display the timetable
        alert("Timetable has been set!"); // Notify the user
        document.getElementById('setTimetablePopup').classList.add('hidden'); // Hide the popup
    }
}
function displayTimetable() {
    const timetable = document.getElementById('timetable');
    timetable.innerHTML = ''; // Clear previous timetable display

    for (const subject in timetableData) {
        const subjectInfo = timetableData[subject];
        const subjectDiv = document.createElement('div');
        subjectDiv.textContent = `${subject}: ${subjectInfo.days.join(', ')} at ${subjectInfo.time}`;
        subjectDiv.className = 'subject';
        timetable.appendChild(subjectDiv);
    }

    // Clear subjects for the next use
    subjects = [];
    document.getElementById('setTimetable').classList.add('hidden'); // Hide the set timetable button
}