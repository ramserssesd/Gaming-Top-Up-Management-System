Step 1: Go to Your Project Folder
	C:\Users\pc\OneDrive\Documents\documents>cd gaming_topup_project_matrix_sols
Step 2: Create a Virtual Environment
	C:\Users\pc\OneDrive\Documents\documents\gaming_topup_project_matrix_sols>python -m venv gaming_project
Step 3: Activate the Virtual Environment
	C:\Users\pc\OneDrive\Documents\documents\gaming_topup_project_matrix_sols\gaming_project>Scripts/Activate
Step 4: Install Django
	pip install django
 pip install rest_framework
Step 5: Run Migrations
	python manage.py makemigrations
	python manage.py migrate
Step 6: Create a Superuser
	python manage.py createsuperuser
Step 7: Run the Server using this command
	python manage.py runserver

API Endpoint :- http://127.0.0.1:8000/api/topup/         method :- POST  content type :- application/json

Sample curl/Postman request :- {
                                  "gamename": "PUBG",
                                  "game_id": "PUBG1",
                                  "product_name": "Moniter",
                                  "product_id": 5,
                                  "product_price": 8000.00,
                                  "user_email": "player@example.com",
                                  "payment_status": "pending"
                                }



