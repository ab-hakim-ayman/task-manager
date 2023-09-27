# task-manager
# Task Manager Web Application with REST API

## Table of Contents
1. [Introduction](#introduction)
2. [Features](#features)
3. [Project Setup](#project-setup)
4. [User Authentication](#user-authentication)
5. [Database Models](#database-models)
6. [Admin Interface](#admin-interface)
7. [Django Templates](#django-templates)
8. [Views and URL Patterns](#views-and-url-patterns)
9. [Functionality Implementation](#functionality-implementation)
10. [REST API](#rest-api)
11. [Git Version Control](#git-version-control)
12. [Environment Variables](#environment-variables)
13. [Documentation](#documentation)
14. [Data Population](#data-population)

## Introduction

The Task Manager is a web application built using Django that allows users to efficiently manage their tasks. It includes a REST API for programmatic access to task data. The application provides features for user authentication, task creation, updating, deletion, and more.

## Features

### User Authentication

- User registration and login functionality are implemented to provide secure access to task management.
- Optionally, a password reset feature is available for user convenience.

### Task Management

- Users can create tasks with the following properties:
  - Title
  - Description
  - Due Date
  - Priority (Low, Medium, High)
  - Completion Status
  - Creation Date
  - Last Update Date (optional)
  - Multiple photos can be added and deleted for each task.
- Tasks can be searched by title and filtered by criteria such as creation date, due date, priority, and completion status.
- Each task has its own details page where all information, including attached photos, is displayed.
- Tasks can be updated, and users have the flexibility to modify all task properties.
- Deletion of tasks is supported with a confirmation step.

### Admin Interface

- The Django admin panel includes the Task model for administrative tasks.
- Only relevant fields are displayed in the admin interface.
- Tasks in the admin panel are sorted by priority by default.

### Django Templates

- The application utilizes Django templates to provide a user-friendly and responsive interface.
- Templates are designed to be visually appealing and user-friendly.

### Views and URL Patterns

- Class-Based Views (CBVs) are used to create the following views:
  - Task list
  - Task creation
  - Task details
  - Task update
  - Task deletion
- URL patterns are defined for each view and mapped to their respective functions.

### Functionality Implementation

- Tasks are fetched from the database and presented in the task list view.
- User-friendly forms are provided for creating and updating tasks, including form validation and error handling.
- Logic for creating, updating, and deleting tasks is implemented using Django's Object-Relational Mapping (ORM).

### REST API

- The application includes a REST API with the following endpoints:
  - List all tasks
  - Retrieve a single task
  - Create a new task
  - Update an existing task
  - Delete a task
- Serializers are used to convert data to and from JSON format.
- The API views handle appropriate HTTP methods and validate input data.

### Git Version Control

- The project is version-controlled using Git for efficient collaboration and code management.
- Commits are made regularly to track project progress.

### Environment Variables

- Sensitive information, such as database credentials, is stored in a separate environment variable file (e.g., `.env`).
- Django is configured to read these environment variables for secure configuration.

### Documentation

- This README file provides comprehensive documentation to help users set up and run the project.
- Instructions for configuring environment variables and other essential details are included.

### Data Population

- The project comes with sample data, including three user accounts and tasks with various priorities and images, to facilitate testing and exploration.

### Data Export

- Data from the database can be exported to JSON fixtures, making it easy to maintain and migrate data.

## Project Setup

1. Clone the repository:
   ```bash
   git clone <repository_url>
