import requests
import json
import logging

logger = logging.getLogger(__name__)

def trigger_webhook_automation(form_data, webhook_url, service_name="Automation"):
    """
    Generic helper to send lead data to a webhook URL (Google Sheets, Zapier, etc.)
    """
    if not webhook_url:
        return False
    
    try:
        payload = {
            "source": "TZaHu Landing Page",
            "service": service_name,
            "data": form_data
        }
        
        response = requests.post(
            webhook_url, 
            json=payload, 
            timeout=10,
            headers={'Content-Type': 'application/json'}
        )
        
        if response.status_code in [200, 201]:
            logger.info(f"Successfully triggered {service_name} automation")
            return True
        else:
            logger.error(f"Failed to trigger {service_name}: Status {response.status_code}")
            return False
            
    except Exception as e:
        logger.error(f"Error in {service_name} automation: {str(e)}")
        return False

def send_to_whatsapp(lead_data, settings):
    """
    Forwards lead data to the WhatsApp webhook
    """
    if not settings or not settings.whatsapp_webhook_url:
        return False
    
    # We add the target number to the data package
    data_with_number = lead_data.copy()
    data_with_number['target_whatsapp'] = settings.whatsapp_number
    
    return trigger_webhook_automation(data_with_number, settings.whatsapp_webhook_url, "WhatsApp")

def send_to_google_sheets(lead_data, settings):
    """
    Forwards lead data to the Google Sheets webhook
    """
    if not settings or not settings.google_sheets_webhook_url:
        return False
        
    return trigger_webhook_automation(lead_data, settings.google_sheets_webhook_url, "Google Sheets")
