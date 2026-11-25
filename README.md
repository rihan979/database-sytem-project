# FIXORA Front-End Demo

A responsive campus issue reporting prototype built with plain HTML, CSS, and JavaScript.

## Run
1. Extract `FIXORA_Frontend.zip`.
2. Open `index.html` in Chrome, Edge, or Firefox.
3. No installation is needed. For editing, open the folder in VS Code (Live Server is optional).

## Working demo features
- Navigation across Overview, All Complaints, Report an Issue, Analytics, and Departments.
- Submit a complaint with category, priority, location, description, and anonymous mode.
- Category-based department routing preview and assignment.
- Search and filter complaints.
- View complaint details and update status.
- Dashboard counts, resolution percentage, priority queue, category/department charts.
- In-app notifications for report submissions and status updates.
- CSV export.
- Browser `localStorage` persists reports on the same browser.

## Important
This is a front-end demo, not a production-ready multi-user system. There is no real authentication, shared database, email sending, or server-side access control. Data is local to the browser and can be edited by the browser user. Sample department email addresses are placeholders. A real deployment needs a backend API, central database (e.g. MySQL/PostgreSQL), password hashing, server-side role-based access control, validated uploads, and audit logging.

## Files
- `index.html`: layout
- `styles.css`: styling and responsive design
- `script.js`: sample data and browser interactions
