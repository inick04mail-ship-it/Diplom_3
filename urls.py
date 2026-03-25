class Urls:
    BASE_URL = "https://stellarburgers.education-services.ru"
    
    
    CREATE_USER = f"{BASE_URL}/api/auth/register"
    DELETE_USER = f"{BASE_URL}/api/auth/user"
    CREATE_ORDER = f"{BASE_URL}/api/orders"
    
   
    VALID_INGREDIENTS = [
        '61c0c5a71d1f82001bdaaa6d',  
        '61c0c5a71d1f82001bdaaa6f',  
        '61c0c5a71d1f82001bdaaa72'   
    ]