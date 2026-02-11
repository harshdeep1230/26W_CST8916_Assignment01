
# **CST8916 - Assignment 1: REST API Extension**

**Student Name:** Harshdeep Puri

**Student ID:**  41170600

**YouTube Demo Link:**  link

---

## **Project Description**

This project is a **Python Flask REST API** designed to manage a task list. It allows users to perform CRUD (Create, Read, Update, Delete) operations on tasks. The application is hosted on **Azure App Service** and tested using the **REST Client** extension in VS Code.

## **Deployment Details**

* **Local URL:** `http://127.0.0.1:5000`
* **Azure Production URL:** `https://[your-app-name].azurewebsites.net`

## **API Endpoints Tested**

I have implemented and tested the following 9 scenarios as required by the assignment:

1. **GET /tasks** - Retrieve all tasks.
2. **GET /tasks/1** - Retrieve a single existing task.
3. **GET /tasks/999** - Handle "Task Not Found" (**404 Error**).
4. **POST /tasks** - Create a new valid task (**201 Created**).
5. **POST /tasks (Invalid)** - Missing required title (**400 Error**).
6. **POST /tasks (Invalid User)** - Non-existent `user_id` (**400 Error**).
7. **PUT /tasks/1** - Update an existing task.
8. **DELETE /tasks/1** - Remove a task (**204 No Content**).
9. **GET /tasks** - Verify deletion.

## **How to Run Locally**

1. Install dependencies: `pip install flask`
2. Run the application: `python app.py`
3. Use `test-tasks-api.http` with the REST Client extension to execute tests.

---

### **Quick Tips for Formatting**

* **Headers:** Use `#` for the main title and `##` for sections.
* **Bold text:** Wrap important words in double asterisks, like `**404 Error**`.
* **Code blocks:** Use backticks (```) around URLs or file names to make them stand out.

**Next Step:** Would you like me to help you double-check your `app.py` code one last time to ensure those 400 and 404 error handlers are working perfectly before you record?

[Documenting a REST API in a README](https://www.youtube.com/watch?v=Swhq665jyZw)

This video provides a walkthrough of a similar Flask deployment and shows how the documentation should look, which is a great reference for your final submission.