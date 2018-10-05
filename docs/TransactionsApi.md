# swagger_client.TransactionsApi

All URIs are relative to *https://api.youneedabudget.com/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_transaction**](TransactionsApi.md#create_transaction) | **POST** /budgets/{budget_id}/transactions | Create a single transaction or multiple transactions
[**get_transaction_by_id**](TransactionsApi.md#get_transaction_by_id) | **GET** /budgets/{budget_id}/transactions/{transaction_id} | Single transaction
[**get_transactions**](TransactionsApi.md#get_transactions) | **GET** /budgets/{budget_id}/transactions | List transactions
[**get_transactions_by_account**](TransactionsApi.md#get_transactions_by_account) | **GET** /budgets/{budget_id}/accounts/{account_id}/transactions | List account transactions
[**get_transactions_by_category**](TransactionsApi.md#get_transactions_by_category) | **GET** /budgets/{budget_id}/categories/{category_id}/transactions | List category transactions
[**get_transactions_by_payee**](TransactionsApi.md#get_transactions_by_payee) | **GET** /budgets/{budget_id}/payees/{payee_id}/transactions | List payee transactions
[**update_transaction**](TransactionsApi.md#update_transaction) | **PUT** /budgets/{budget_id}/transactions/{transaction_id} | Updates an existing transaction


# **create_transaction**
> SaveTransactionsResponse create_transaction(budget_id, save_transactions)

Create a single transaction or multiple transactions

Creates a single transaction or multiple transactions.  If you provide a body containing a 'transaction' object, a single transaction will be created and if you provide a body containing a 'transactions' array, multiple transactions will be created.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: bearer
configuration = swagger_client.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.TransactionsApi(swagger_client.ApiClient(configuration))
budget_id = swagger_client.ERRORUNKNOWN() # ERRORUNKNOWN | The id of the budget (\"last-used\" can also be used to specify the last used budget)
save_transactions = swagger_client.SaveTransactionsWrapper() # SaveTransactionsWrapper | The transaction or transactions to create

try:
    # Create a single transaction or multiple transactions
    api_response = api_instance.create_transaction(budget_id, save_transactions)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TransactionsApi->create_transaction: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **budget_id** | [**ERRORUNKNOWN**](.md)| The id of the budget (\&quot;last-used\&quot; can also be used to specify the last used budget) | 
 **save_transactions** | [**SaveTransactionsWrapper**](SaveTransactionsWrapper.md)| The transaction or transactions to create | 

### Return type

[**SaveTransactionsResponse**](SaveTransactionsResponse.md)

### Authorization

[bearer](../README.md#bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_transaction_by_id**
> TransactionResponse get_transaction_by_id(budget_id, transaction_id)

Single transaction

Returns a single transaction

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: bearer
configuration = swagger_client.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.TransactionsApi(swagger_client.ApiClient(configuration))
budget_id = swagger_client.ERRORUNKNOWN() # ERRORUNKNOWN | The id of the budget (\"last-used\" can also be used to specify the last used budget)
transaction_id = swagger_client.ERRORUNKNOWN() # ERRORUNKNOWN | The id of the transaction

try:
    # Single transaction
    api_response = api_instance.get_transaction_by_id(budget_id, transaction_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TransactionsApi->get_transaction_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **budget_id** | [**ERRORUNKNOWN**](.md)| The id of the budget (\&quot;last-used\&quot; can also be used to specify the last used budget) | 
 **transaction_id** | [**ERRORUNKNOWN**](.md)| The id of the transaction | 

### Return type

[**TransactionResponse**](TransactionResponse.md)

### Authorization

[bearer](../README.md#bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_transactions**
> TransactionsResponse get_transactions(budget_id, since_date=since_date, type=type)

List transactions

Returns budget transactions

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: bearer
configuration = swagger_client.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.TransactionsApi(swagger_client.ApiClient(configuration))
budget_id = swagger_client.ERRORUNKNOWN() # ERRORUNKNOWN | The id of the budget (\"last-used\" can also be used to specify the last used budget)
since_date = swagger_client.ERRORUNKNOWN() # ERRORUNKNOWN | Only return transactions on or after this date (optional)
type = swagger_client.ERRORUNKNOWN() # ERRORUNKNOWN | Only return transactions of a certain type ('uncategorized' and 'unapproved' are currently supported) (optional)

try:
    # List transactions
    api_response = api_instance.get_transactions(budget_id, since_date=since_date, type=type)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TransactionsApi->get_transactions: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **budget_id** | [**ERRORUNKNOWN**](.md)| The id of the budget (\&quot;last-used\&quot; can also be used to specify the last used budget) | 
 **since_date** | [**ERRORUNKNOWN**](.md)| Only return transactions on or after this date | [optional] 
 **type** | [**ERRORUNKNOWN**](.md)| Only return transactions of a certain type (&#39;uncategorized&#39; and &#39;unapproved&#39; are currently supported) | [optional] 

### Return type

[**TransactionsResponse**](TransactionsResponse.md)

### Authorization

[bearer](../README.md#bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_transactions_by_account**
> TransactionsResponse get_transactions_by_account(budget_id, account_id, since_date=since_date, type=type)

List account transactions

Returns all transactions for a specified account

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: bearer
configuration = swagger_client.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.TransactionsApi(swagger_client.ApiClient(configuration))
budget_id = swagger_client.ERRORUNKNOWN() # ERRORUNKNOWN | The id of the budget (\"last-used\" can also be used to specify the last used budget)
account_id = swagger_client.ERRORUNKNOWN() # ERRORUNKNOWN | The id of the account
since_date = swagger_client.ERRORUNKNOWN() # ERRORUNKNOWN | Only return transactions on or after this date (optional)
type = swagger_client.ERRORUNKNOWN() # ERRORUNKNOWN | Only return transactions of a certain type (i.e. 'uncategorized', 'unapproved') (optional)

try:
    # List account transactions
    api_response = api_instance.get_transactions_by_account(budget_id, account_id, since_date=since_date, type=type)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TransactionsApi->get_transactions_by_account: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **budget_id** | [**ERRORUNKNOWN**](.md)| The id of the budget (\&quot;last-used\&quot; can also be used to specify the last used budget) | 
 **account_id** | [**ERRORUNKNOWN**](.md)| The id of the account | 
 **since_date** | [**ERRORUNKNOWN**](.md)| Only return transactions on or after this date | [optional] 
 **type** | [**ERRORUNKNOWN**](.md)| Only return transactions of a certain type (i.e. &#39;uncategorized&#39;, &#39;unapproved&#39;) | [optional] 

### Return type

[**TransactionsResponse**](TransactionsResponse.md)

### Authorization

[bearer](../README.md#bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_transactions_by_category**
> HybridTransactionsResponse get_transactions_by_category(budget_id, category_id, since_date=since_date, type=type)

List category transactions

Returns all transactions for a specified category

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: bearer
configuration = swagger_client.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.TransactionsApi(swagger_client.ApiClient(configuration))
budget_id = swagger_client.ERRORUNKNOWN() # ERRORUNKNOWN | The id of the budget (\"last-used\" can also be used to specify the last used budget)
category_id = swagger_client.ERRORUNKNOWN() # ERRORUNKNOWN | The id of the category
since_date = swagger_client.ERRORUNKNOWN() # ERRORUNKNOWN | Only return transactions on or after this date (optional)
type = swagger_client.ERRORUNKNOWN() # ERRORUNKNOWN | Only return transactions of a certain type (i.e. 'uncategorized', 'unapproved') (optional)

try:
    # List category transactions
    api_response = api_instance.get_transactions_by_category(budget_id, category_id, since_date=since_date, type=type)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TransactionsApi->get_transactions_by_category: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **budget_id** | [**ERRORUNKNOWN**](.md)| The id of the budget (\&quot;last-used\&quot; can also be used to specify the last used budget) | 
 **category_id** | [**ERRORUNKNOWN**](.md)| The id of the category | 
 **since_date** | [**ERRORUNKNOWN**](.md)| Only return transactions on or after this date | [optional] 
 **type** | [**ERRORUNKNOWN**](.md)| Only return transactions of a certain type (i.e. &#39;uncategorized&#39;, &#39;unapproved&#39;) | [optional] 

### Return type

[**HybridTransactionsResponse**](HybridTransactionsResponse.md)

### Authorization

[bearer](../README.md#bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_transactions_by_payee**
> HybridTransactionsResponse get_transactions_by_payee(budget_id, payee_id, since_date=since_date, type=type)

List payee transactions

Returns all transactions for a specified payee

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: bearer
configuration = swagger_client.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.TransactionsApi(swagger_client.ApiClient(configuration))
budget_id = swagger_client.ERRORUNKNOWN() # ERRORUNKNOWN | The id of the budget (\"last-used\" can also be used to specify the last used budget)
payee_id = swagger_client.ERRORUNKNOWN() # ERRORUNKNOWN | The id of the payee
since_date = swagger_client.ERRORUNKNOWN() # ERRORUNKNOWN | Only return transactions on or after this date (optional)
type = swagger_client.ERRORUNKNOWN() # ERRORUNKNOWN | Only return transactions of a certain type (i.e. 'uncategorized', 'unapproved') (optional)

try:
    # List payee transactions
    api_response = api_instance.get_transactions_by_payee(budget_id, payee_id, since_date=since_date, type=type)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TransactionsApi->get_transactions_by_payee: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **budget_id** | [**ERRORUNKNOWN**](.md)| The id of the budget (\&quot;last-used\&quot; can also be used to specify the last used budget) | 
 **payee_id** | [**ERRORUNKNOWN**](.md)| The id of the payee | 
 **since_date** | [**ERRORUNKNOWN**](.md)| Only return transactions on or after this date | [optional] 
 **type** | [**ERRORUNKNOWN**](.md)| Only return transactions of a certain type (i.e. &#39;uncategorized&#39;, &#39;unapproved&#39;) | [optional] 

### Return type

[**HybridTransactionsResponse**](HybridTransactionsResponse.md)

### Authorization

[bearer](../README.md#bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_transaction**
> TransactionResponse update_transaction(budget_id, transaction_id, transaction)

Updates an existing transaction

Updates a transaction

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: bearer
configuration = swagger_client.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.TransactionsApi(swagger_client.ApiClient(configuration))
budget_id = swagger_client.ERRORUNKNOWN() # ERRORUNKNOWN | The id of the budget (\"last-used\" can also be used to specify the last used budget)
transaction_id = swagger_client.ERRORUNKNOWN() # ERRORUNKNOWN | The id of the transaction
transaction = swagger_client.SaveTransactionWrapper() # SaveTransactionWrapper | The transaction to update

try:
    # Updates an existing transaction
    api_response = api_instance.update_transaction(budget_id, transaction_id, transaction)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TransactionsApi->update_transaction: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **budget_id** | [**ERRORUNKNOWN**](.md)| The id of the budget (\&quot;last-used\&quot; can also be used to specify the last used budget) | 
 **transaction_id** | [**ERRORUNKNOWN**](.md)| The id of the transaction | 
 **transaction** | [**SaveTransactionWrapper**](SaveTransactionWrapper.md)| The transaction to update | 

### Return type

[**TransactionResponse**](TransactionResponse.md)

### Authorization

[bearer](../README.md#bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

