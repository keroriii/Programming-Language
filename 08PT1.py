def session_counter():
    """Simulates a per-session counter with stack-dynamic variable"""
    counter = 0  
    counter += 1
    print(f"Session visits: {counter}")

def kiosk_usage():
    """Simulates a persistent usage tracker with static-like variable"""
    if not hasattr(kiosk_usage, 'total_users'):
        kiosk_usage.total_users = 0  
    kiosk_usage.total_users += 1
    print(f"Total users today: {kiosk_usage.total_users}")

def main():
    """Main program to simulate three customer sessions""" 
    print("Starting Kiosk System Simulation")
    print("\n=== Customer 1 ===")
    session_counter()  
    kiosk_usage()     
    
    print("\n=== Customer 2 ===")
    session_counter() 
    kiosk_usage()      
    
    print("\n=== Customer 3 ===")
    session_counter()  
    kiosk_usage()     
    
 
    print("\nDemonstrating session_counter reset behavior:")
    for i in range(5):
        session_counter() 

if __name__ == "__main__":
    main()