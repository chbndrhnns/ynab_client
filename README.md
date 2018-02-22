# swagger-client
Our API uses a REST based design, leverages the JSON data format, and relies upon HTTPS for transport. We respond with meaningful HTTP response codes and if an error occurs, we include error details in the response body.  API Documentation is at https://api.youneedabudget.com

This Python package is automatically generated by the [Swagger Codegen](https://github.com/swagger-api/swagger-codegen) project:

- API version: 1.0.0
- Package version: 1.0.0
- Build package: io.swagger.codegen.languages.PythonClientCodegen

## Requirements.

Python 2.7 and 3.4+

## Installation & Usage
### pip install

If the python package is hosted on Github, you can install directly from Github

```sh
pip install git+https://github.com/GIT_USER_ID/GIT_REPO_ID.git
```
(you may need to run `pip` with root permission: `sudo pip install git+https://github.com/GIT_USER_ID/GIT_REPO_ID.git`)

Then import the package:
```python
import swagger_client 
```

### Setuptools

Install via [Setuptools](http://pypi.python.org/pypi/setuptools).

```sh
python setup.py install --user
```
(or `sudo python setup.py install` to install the package for all users)

Then import the package:
```python
import swagger_client
```

## Getting Started

Please follow the [installation procedure](#installation--usage) and then run the following:

```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: bearer
swagger_client.configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# swagger_client.configuration.api_key_prefix['Authorization'] = 'Bearer'
# create an instance of the API class
api_instance = swagger_client.AccountsApi()
budget_id = 'budget_id_example' # str | The ID of the Budget.
account_id = 'account_id_example' # str | The ID of the Account.

try:
    # Single account
    api_response = api_instance.get_account_by_id(budget_id, account_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AccountsApi->get_account_by_id: %s\n" % e)

```

## Documentation for API Endpoints

All URIs are relative to *https://api.youneedabudget.com/v1*

Class | Method | HTTP request | Description
------------ | ------------- | ------------- | -------------
*AccountsApi* | [**get_account_by_id**](docs/AccountsApi.md#get_account_by_id) | **GET** /budgets/{budget_id}/accounts/{account_id} | Single account
*AccountsApi* | [**get_accounts**](docs/AccountsApi.md#get_accounts) | **GET** /budgets/{budget_id}/accounts | Account list
*BudgetsApi* | [**get_budget_by_id**](docs/BudgetsApi.md#get_budget_by_id) | **GET** /budgets/{budget_id} | Single budget
*BudgetsApi* | [**get_budgets**](docs/BudgetsApi.md#get_budgets) | **GET** /budgets | List budgets
*CategoriesApi* | [**get_categories**](docs/CategoriesApi.md#get_categories) | **GET** /budgets/{budget_id}/categories | List categories
*CategoriesApi* | [**get_category_by_id**](docs/CategoriesApi.md#get_category_by_id) | **GET** /budgets/{budget_id}/categories/{category_id} | Single category
*MonthsApi* | [**get_budget_month**](docs/MonthsApi.md#get_budget_month) | **GET** /budgets/{budget_id}/months/{month} | Single budget month
*MonthsApi* | [**get_budget_months**](docs/MonthsApi.md#get_budget_months) | **GET** /budgets/{budget_id}/months | List budget months
*PayeeLocationsApi* | [**get_payee_location_by_id**](docs/PayeeLocationsApi.md#get_payee_location_by_id) | **GET** /budgets/{budget_id}/payee_locations/{payee_location_id} | Single payee location
*PayeeLocationsApi* | [**get_payee_locations**](docs/PayeeLocationsApi.md#get_payee_locations) | **GET** /budgets/{budget_id}/payee_locations | List payee locations
*PayeeLocationsApi* | [**get_payee_locations_by_payee**](docs/PayeeLocationsApi.md#get_payee_locations_by_payee) | **GET** /budgets/{budget_id}/payees/{payee_id}/payee_locations | List locations for a payee
*PayeesApi* | [**get_payee_by_id**](docs/PayeesApi.md#get_payee_by_id) | **GET** /budgets/{budget_id}/payees/{payee_id} | Single payee
*PayeesApi* | [**get_payees**](docs/PayeesApi.md#get_payees) | **GET** /budgets/{budget_id}/payees | List payees
*ScheduledTransactionsApi* | [**get_scheduled_transaction_by_id**](docs/ScheduledTransactionsApi.md#get_scheduled_transaction_by_id) | **GET** /budgets/{budget_id}/scheduled_transactions/{scheduled_transaction_id} | Single scheduled transaction
*ScheduledTransactionsApi* | [**get_scheduled_transactions**](docs/ScheduledTransactionsApi.md#get_scheduled_transactions) | **GET** /budgets/{budget_id}/scheduled_transactions | List scheduled transactions
*TransactionsApi* | [**bulk_create_transactions**](docs/TransactionsApi.md#bulk_create_transactions) | **POST** /budgets/{budget_id}/transactions/bulk | Bulk create transactions
*TransactionsApi* | [**create_transaction**](docs/TransactionsApi.md#create_transaction) | **POST** /budgets/{budget_id}/transactions | Create new transaction
*TransactionsApi* | [**get_transactions**](docs/TransactionsApi.md#get_transactions) | **GET** /budgets/{budget_id}/transactions | List transactions
*TransactionsApi* | [**get_transactions_by_account**](docs/TransactionsApi.md#get_transactions_by_account) | **GET** /budgets/{budget_id}/accounts/{account_id}/transactions | List account transactions
*TransactionsApi* | [**get_transactions_by_category**](docs/TransactionsApi.md#get_transactions_by_category) | **GET** /budgets/{budget_id}/categories/{category_id}/transactions | List category transactions
*TransactionsApi* | [**get_transactions_by_id**](docs/TransactionsApi.md#get_transactions_by_id) | **GET** /budgets/{budget_id}/transactions/{transaction_id} | Single transaction
*TransactionsApi* | [**update_transaction**](docs/TransactionsApi.md#update_transaction) | **PUT** /budgets/{budget_id}/transactions/{transaction_id} | Updates an existing transaction


## Documentation For Models

 - [Account](docs/Account.md)
 - [AccountResponse](docs/AccountResponse.md)
 - [AccountWrapper](docs/AccountWrapper.md)
 - [AccountsResponse](docs/AccountsResponse.md)
 - [AccountsWrapper](docs/AccountsWrapper.md)
 - [BudgetDetailResponse](docs/BudgetDetailResponse.md)
 - [BudgetDetailWrapper](docs/BudgetDetailWrapper.md)
 - [BudgetSummary](docs/BudgetSummary.md)
 - [BudgetSummaryResponse](docs/BudgetSummaryResponse.md)
 - [BudgetSummaryWrapper](docs/BudgetSummaryWrapper.md)
 - [BulkIdWrapper](docs/BulkIdWrapper.md)
 - [BulkIds](docs/BulkIds.md)
 - [BulkResponse](docs/BulkResponse.md)
 - [BulkTransactions](docs/BulkTransactions.md)
 - [CategoriesResponse](docs/CategoriesResponse.md)
 - [Category](docs/Category.md)
 - [CategoryGroup](docs/CategoryGroup.md)
 - [CategoryGroupsWrapper](docs/CategoryGroupsWrapper.md)
 - [CategoryResponse](docs/CategoryResponse.md)
 - [CategoryWrapper](docs/CategoryWrapper.md)
 - [CurrencyFormat](docs/CurrencyFormat.md)
 - [DateFormat](docs/DateFormat.md)
 - [ErrorDetail](docs/ErrorDetail.md)
 - [ErrorResponse](docs/ErrorResponse.md)
 - [MonthDetailResponse](docs/MonthDetailResponse.md)
 - [MonthDetailWrapper](docs/MonthDetailWrapper.md)
 - [MonthSummariesResponse](docs/MonthSummariesResponse.md)
 - [MonthSummariesWrapper](docs/MonthSummariesWrapper.md)
 - [MonthSummary](docs/MonthSummary.md)
 - [Payee](docs/Payee.md)
 - [PayeeLocation](docs/PayeeLocation.md)
 - [PayeeLocationResponse](docs/PayeeLocationResponse.md)
 - [PayeeLocationWrapper](docs/PayeeLocationWrapper.md)
 - [PayeeLocationsResponse](docs/PayeeLocationsResponse.md)
 - [PayeeLocationsWrapper](docs/PayeeLocationsWrapper.md)
 - [PayeeResponse](docs/PayeeResponse.md)
 - [PayeeWrapper](docs/PayeeWrapper.md)
 - [PayeesResponse](docs/PayeesResponse.md)
 - [PayeesWrapper](docs/PayeesWrapper.md)
 - [SaveTransaction](docs/SaveTransaction.md)
 - [SaveTransactionWrapper](docs/SaveTransactionWrapper.md)
 - [ScheduledSubTransaction](docs/ScheduledSubTransaction.md)
 - [ScheduledTransactionResponse](docs/ScheduledTransactionResponse.md)
 - [ScheduledTransactionSummary](docs/ScheduledTransactionSummary.md)
 - [ScheduledTransactionWrapper](docs/ScheduledTransactionWrapper.md)
 - [ScheduledTransactionsResponse](docs/ScheduledTransactionsResponse.md)
 - [ScheduledTransactionsWrapper](docs/ScheduledTransactionsWrapper.md)
 - [SubTransaction](docs/SubTransaction.md)
 - [TransactionResponse](docs/TransactionResponse.md)
 - [TransactionSummary](docs/TransactionSummary.md)
 - [TransactionWrapper](docs/TransactionWrapper.md)
 - [TransactionsResponse](docs/TransactionsResponse.md)
 - [TransactionsWrapper](docs/TransactionsWrapper.md)
 - [BudgetDetail](docs/BudgetDetail.md)
 - [CategoryGroupWithCategories](docs/CategoryGroupWithCategories.md)
 - [MonthDetail](docs/MonthDetail.md)
 - [ScheduledTransactionDetail](docs/ScheduledTransactionDetail.md)
 - [TransactionDetail](docs/TransactionDetail.md)


## Documentation For Authorization


## bearer

- **Type**: API key
- **API key parameter name**: Authorization
- **Location**: HTTP header


## Author



