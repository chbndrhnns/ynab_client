# coding: utf-8

"""
    YNAB API Endpoints

    Our API uses a REST based design, leverages the JSON data format, and relies upon HTTPS for transport. We respond with meaningful HTTP response codes and if an error occurs, we include error details in the response body.  API Documentation is at https://api.youneedabudget.com  # noqa: E501

    OpenAPI spec version: 1.0.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six


class TransactionSummary(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'id': 'str',
        '_date': 'date',
        'amount': 'int',
        'memo': 'str',
        'cleared': 'str',
        'approved': 'bool',
        'flag_color': 'str',
        'account_id': 'str',
        'payee_id': 'str',
        'category_id': 'str',
        'transfer_account_id': 'str',
        'import_id': 'str',
        'deleted': 'bool'
    }

    attribute_map = {
        'id': 'id',
        '_date': 'date',
        'amount': 'amount',
        'memo': 'memo',
        'cleared': 'cleared',
        'approved': 'approved',
        'flag_color': 'flag_color',
        'account_id': 'account_id',
        'payee_id': 'payee_id',
        'category_id': 'category_id',
        'transfer_account_id': 'transfer_account_id',
        'import_id': 'import_id',
        'deleted': 'deleted'
    }

    def __init__(self, id=None, _date=None, amount=None, memo=None, cleared=None, approved=None, flag_color=None, account_id=None, payee_id=None, category_id=None, transfer_account_id=None, import_id=None, deleted=None):  # noqa: E501
        """TransactionSummary - a model defined in Swagger"""  # noqa: E501

        self._id = None
        self.__date = None
        self._amount = None
        self._memo = None
        self._cleared = None
        self._approved = None
        self._flag_color = None
        self._account_id = None
        self._payee_id = None
        self._category_id = None
        self._transfer_account_id = None
        self._import_id = None
        self._deleted = None
        self.discriminator = None

        self.id = id
        self._date = _date
        self.amount = amount
        self.memo = memo
        self.cleared = cleared
        self.approved = approved
        self.flag_color = flag_color
        self.account_id = account_id
        self.payee_id = payee_id
        self.category_id = category_id
        self.transfer_account_id = transfer_account_id
        self.import_id = import_id
        self.deleted = deleted

    @property
    def id(self):
        """Gets the id of this TransactionSummary.  # noqa: E501


        :return: The id of this TransactionSummary.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this TransactionSummary.


        :param id: The id of this TransactionSummary.  # noqa: E501
        :type: str
        """
        if id is None:
            raise ValueError("Invalid value for `id`, must not be `None`")  # noqa: E501

        self._id = id

    @property
    def _date(self):
        """Gets the _date of this TransactionSummary.  # noqa: E501


        :return: The _date of this TransactionSummary.  # noqa: E501
        :rtype: date
        """
        return self.__date

    @_date.setter
    def _date(self, _date):
        """Sets the _date of this TransactionSummary.


        :param _date: The _date of this TransactionSummary.  # noqa: E501
        :type: date
        """
        if _date is None:
            raise ValueError("Invalid value for `_date`, must not be `None`")  # noqa: E501

        self.__date = _date

    @property
    def amount(self):
        """Gets the amount of this TransactionSummary.  # noqa: E501

        The transaction amount in milliunits format  # noqa: E501

        :return: The amount of this TransactionSummary.  # noqa: E501
        :rtype: int
        """
        return self._amount

    @amount.setter
    def amount(self, amount):
        """Sets the amount of this TransactionSummary.

        The transaction amount in milliunits format  # noqa: E501

        :param amount: The amount of this TransactionSummary.  # noqa: E501
        :type: int
        """
        if amount is None:
            raise ValueError("Invalid value for `amount`, must not be `None`")  # noqa: E501

        self._amount = amount

    @property
    def memo(self):
        """Gets the memo of this TransactionSummary.  # noqa: E501


        :return: The memo of this TransactionSummary.  # noqa: E501
        :rtype: str
        """
        return self._memo

    @memo.setter
    def memo(self, memo):
        """Sets the memo of this TransactionSummary.


        :param memo: The memo of this TransactionSummary.  # noqa: E501
        :type: str
        """
        if memo is None:
            raise ValueError("Invalid value for `memo`, must not be `None`")  # noqa: E501

        self._memo = memo

    @property
    def cleared(self):
        """Gets the cleared of this TransactionSummary.  # noqa: E501

        The cleared status of the transaction  # noqa: E501

        :return: The cleared of this TransactionSummary.  # noqa: E501
        :rtype: str
        """
        return self._cleared

    @cleared.setter
    def cleared(self, cleared):
        """Sets the cleared of this TransactionSummary.

        The cleared status of the transaction  # noqa: E501

        :param cleared: The cleared of this TransactionSummary.  # noqa: E501
        :type: str
        """
        if cleared is None:
            raise ValueError("Invalid value for `cleared`, must not be `None`")  # noqa: E501
        allowed_values = ["cleared", "uncleared", "reconciled"]  # noqa: E501
        if cleared not in allowed_values:
            raise ValueError(
                "Invalid value for `cleared` ({0}), must be one of {1}"  # noqa: E501
                .format(cleared, allowed_values)
            )

        self._cleared = cleared

    @property
    def approved(self):
        """Gets the approved of this TransactionSummary.  # noqa: E501

        Whether or not the transaction is approved  # noqa: E501

        :return: The approved of this TransactionSummary.  # noqa: E501
        :rtype: bool
        """
        return self._approved

    @approved.setter
    def approved(self, approved):
        """Sets the approved of this TransactionSummary.

        Whether or not the transaction is approved  # noqa: E501

        :param approved: The approved of this TransactionSummary.  # noqa: E501
        :type: bool
        """
        if approved is None:
            raise ValueError("Invalid value for `approved`, must not be `None`")  # noqa: E501

        self._approved = approved

    @property
    def flag_color(self):
        """Gets the flag_color of this TransactionSummary.  # noqa: E501

        The transaction flag  # noqa: E501

        :return: The flag_color of this TransactionSummary.  # noqa: E501
        :rtype: str
        """
        return self._flag_color

    @flag_color.setter
    def flag_color(self, flag_color):
        """Sets the flag_color of this TransactionSummary.

        The transaction flag  # noqa: E501

        :param flag_color: The flag_color of this TransactionSummary.  # noqa: E501
        :type: str
        """
        if flag_color is None:
            raise ValueError("Invalid value for `flag_color`, must not be `None`")  # noqa: E501
        allowed_values = ["red", "orange", "yellow", "green", "blue", "purple"]  # noqa: E501
        if flag_color not in allowed_values:
            raise ValueError(
                "Invalid value for `flag_color` ({0}), must be one of {1}"  # noqa: E501
                .format(flag_color, allowed_values)
            )

        self._flag_color = flag_color

    @property
    def account_id(self):
        """Gets the account_id of this TransactionSummary.  # noqa: E501


        :return: The account_id of this TransactionSummary.  # noqa: E501
        :rtype: str
        """
        return self._account_id

    @account_id.setter
    def account_id(self, account_id):
        """Sets the account_id of this TransactionSummary.


        :param account_id: The account_id of this TransactionSummary.  # noqa: E501
        :type: str
        """
        if account_id is None:
            raise ValueError("Invalid value for `account_id`, must not be `None`")  # noqa: E501

        self._account_id = account_id

    @property
    def payee_id(self):
        """Gets the payee_id of this TransactionSummary.  # noqa: E501


        :return: The payee_id of this TransactionSummary.  # noqa: E501
        :rtype: str
        """
        return self._payee_id

    @payee_id.setter
    def payee_id(self, payee_id):
        """Sets the payee_id of this TransactionSummary.


        :param payee_id: The payee_id of this TransactionSummary.  # noqa: E501
        :type: str
        """
        if payee_id is None:
            raise ValueError("Invalid value for `payee_id`, must not be `None`")  # noqa: E501

        self._payee_id = payee_id

    @property
    def category_id(self):
        """Gets the category_id of this TransactionSummary.  # noqa: E501


        :return: The category_id of this TransactionSummary.  # noqa: E501
        :rtype: str
        """
        return self._category_id

    @category_id.setter
    def category_id(self, category_id):
        """Sets the category_id of this TransactionSummary.


        :param category_id: The category_id of this TransactionSummary.  # noqa: E501
        :type: str
        """
        if category_id is None:
            raise ValueError("Invalid value for `category_id`, must not be `None`")  # noqa: E501

        self._category_id = category_id

    @property
    def transfer_account_id(self):
        """Gets the transfer_account_id of this TransactionSummary.  # noqa: E501


        :return: The transfer_account_id of this TransactionSummary.  # noqa: E501
        :rtype: str
        """
        return self._transfer_account_id

    @transfer_account_id.setter
    def transfer_account_id(self, transfer_account_id):
        """Sets the transfer_account_id of this TransactionSummary.


        :param transfer_account_id: The transfer_account_id of this TransactionSummary.  # noqa: E501
        :type: str
        """
        if transfer_account_id is None:
            raise ValueError("Invalid value for `transfer_account_id`, must not be `None`")  # noqa: E501

        self._transfer_account_id = transfer_account_id

    @property
    def import_id(self):
        """Gets the import_id of this TransactionSummary.  # noqa: E501

        If the Transaction was imported, this field is a unique (by account) import identifier.  If this transaction was imported through File Based Import or Direct Import and not through the API, the import_id will have the format: 'YNAB:[milliunit_amount]:[iso_date]:[occurrence]'.  For example, a transaction dated 2015-12-30 in the amount of -$294.23 USD would have an import_id of 'YNAB:-294230:2015-12-30:1'.  If a second transaction on the same account was imported and had the same date and same amount, its import_id would be 'YNAB:-294230:2015-12-30:2'.  # noqa: E501

        :return: The import_id of this TransactionSummary.  # noqa: E501
        :rtype: str
        """
        return self._import_id

    @import_id.setter
    def import_id(self, import_id):
        """Sets the import_id of this TransactionSummary.

        If the Transaction was imported, this field is a unique (by account) import identifier.  If this transaction was imported through File Based Import or Direct Import and not through the API, the import_id will have the format: 'YNAB:[milliunit_amount]:[iso_date]:[occurrence]'.  For example, a transaction dated 2015-12-30 in the amount of -$294.23 USD would have an import_id of 'YNAB:-294230:2015-12-30:1'.  If a second transaction on the same account was imported and had the same date and same amount, its import_id would be 'YNAB:-294230:2015-12-30:2'.  # noqa: E501

        :param import_id: The import_id of this TransactionSummary.  # noqa: E501
        :type: str
        """
        if import_id is None:
            raise ValueError("Invalid value for `import_id`, must not be `None`")  # noqa: E501

        self._import_id = import_id

    @property
    def deleted(self):
        """Gets the deleted of this TransactionSummary.  # noqa: E501

        Whether or not the transaction has been deleted.  Deleted transactions will only be included in delta requests.  # noqa: E501

        :return: The deleted of this TransactionSummary.  # noqa: E501
        :rtype: bool
        """
        return self._deleted

    @deleted.setter
    def deleted(self, deleted):
        """Sets the deleted of this TransactionSummary.

        Whether or not the transaction has been deleted.  Deleted transactions will only be included in delta requests.  # noqa: E501

        :param deleted: The deleted of this TransactionSummary.  # noqa: E501
        :type: bool
        """
        if deleted is None:
            raise ValueError("Invalid value for `deleted`, must not be `None`")  # noqa: E501

        self._deleted = deleted

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.swagger_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value
        if issubclass(TransactionSummary, dict):
            for key, value in self.items():
                result[key] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, TransactionSummary):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
