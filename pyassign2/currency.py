#Assignment2, exchange
#韦宗乐，1700011705
#2017.12.11
"""Module for currency exchange

This module provides several string parsing functions to implement a 
simple currency exchange routine using an online currency service. 
The primary function in this module is exchange."""

def exchange(currency_from, currency_to, amount_from):
    """Returns: amount of currency received in the given exchange.

    In this exchange, the user is changing amount_from money in 
    currency currency_from to the currency currency_to. The value 
    returned represents the amount in currency currency_to. If the
    currency code or amount entered is invalid, it will shows an
    error description.

    The value returned has type float.

    Parameter currency_from: the currency on hand
    Precondition: currency_from is a string for a valid currency code

    Parameter currency_to: the currency to convert to
    Precondition: currency_to is a string for a valid currency code

    Parameter amount_from: amount of currency to convert
    Precondition: amount_from is a float
    """
    
    jstr = url_result(currency_from, currency_to, amount_from)
    
    if not has_error(jstr):
        result = sep_str(jstr)
        amount_to = float(result)
        return amount_to
    
    else:
        print(error_content(jstr))
        return None

        

def url_result(currency_from, currency_to, amount_from):
    """Returns: a string of the web exchanging result
    
    This function gives the three parameter currency_from, currency_to 
    and amount_from to the URL. Then it receives a byte flow from the 
    URL, which is the result. Finally, this function change the byte 
    flow into a string flow, and return the string.
    
    The value returned has type str.
    
    Parameter currency_from: the currency on hand
    Precondition: currency_from is a string for a valid currency code

    Parameter currency_to: the currency to convert to
    Precondition: currency_to is a string for a valid currency code

    Parameter amount_from: amount of currency to convert
    Precondition: amount_from is a float
    """    
    
    from urllib.request import urlopen
    
    doc = urlopen('http://cs1110.cs.cornell.edu/2016fa/a1server.php?from='+
                  currency_from + '&to=' + currency_to + '&amt=' + amount_from)
    docstr = doc.read()
    doc.close()
    jstr = docstr.decode('ascii')
    
    return jstr
    
    
def sep_str(url_text):
    """Returns: a text shows the amount of currency received in given exchange.
    
    This function extract the amount of currency received in the
    given exchange from the whole text which the URL returns.
    
    The return value has type str.
    
    Parameter url_text: text returned from URL
    Precondition: url_text is a string written in a particularly format.
    """
    
    a_list = url_text.split(':')
    wd_list = a_list[2].split()
    result = wd_list[0].lstrip('"')
    
    return result


def has_error(url_text):
    """Returns: True if the url result does not show succeeding, False if shows.
    
    This function judges whether the URL returns an error
    in the text. If there is an error, this function returns
    True. If not, it returns False.
    
    The return value has type bool.
    
    Parameter url_text: text returned from URL
    Precondition: url_text is a string written in a particularly format.
    """
    
    a_list = url_text.split(',')
    wd_list = a_list[2].split()
    judge = wd_list[2]
    if judge == 'true':
        return False
    else:
        return True
    
    
def error_content(url_text):
    """Returns: the error description from the URL
    
    This function extract the error description from the whole text which 
    the URL returns. There are 4 conditions: 'Source currency code is invalid',
    'Exchange currency code is invalid.', 'Currency amount is invalid.', and 
    ''(an empty string) if there is no error. Besides, because the URL judges
    from left to right, if there are more than 1 errors, the URL only shows
    the first one (Source > Exchange > Currency amount).
    
    The value returned has type str.
    
    Parameter url_text: text returned from URL
    Precondition: url_text is a string written in a particularly format.
    """
    
    a_list = url_text.split(',')
    wd_list = a_list[3].split(':')
    error_text = wd_list[1].strip('" }')
    return error_text

    
# Below are test functions    
def test_url_result():
    """Test for function url_result"""
    
    assert ('{ "from" : "7 Chinese Yuan", "to" : "1.0726078928618 United States'
            + ' Dollars", "success" : true, "error" : "" }' 
            == url_result('CNY', 'USD', '7'))
    

def test_sep_str(): 
    """Test for function sep_str"""

    assert sep_str(url_result('CNY', 'USD', '7')) == '1.0726078928618'


def test_has_error():
    """Test for function has_error"""
    
    assert has_error(url_result('CNY', 'USD', '7')) == False
    assert has_error(url_result('CNY', 'UtSD', '7')) == True
    assert has_error(url_result('20CNY', 'USD', '7')) == True
    assert has_error(url_result('CNY', 'USD', '7q')) == True
    

def test_error_content():
    """Test for function error_content"""
    
    assert (error_content(url_result('CNY', 'UtSD', '7')) 
            == 'Exchange currency code is invalid.')
    assert (error_content(url_result('20CNY', 'USD', '7')) 
            == 'Source currency code is invalid.')
    assert (error_content(url_result('CNY', 'USD', '7q')) 
            == 'Currency amount is invalid.')
    assert (error_content(url_result('CNY', 'USD', '7')) 
            == '')
    

def test_exchange():
    """Test for function exchange"""
    
    assert exchange('CNY', 'USD', '7') == 1.0726078928618
    

def test_all():
    """Unit test for module exchange"""
    
    test_url_result()
    test_sep_str()
    test_has_error()
    test_error_content()
    test_exchange()
    
    print("All tests passed.")


def main():
    """main module"""
    test_all()


if __name__ == '__main__':
    main()
