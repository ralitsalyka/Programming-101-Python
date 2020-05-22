from datetime import datetime

def get_booking_status(booking):
    now = datetime.now()

    if booking.cancelled:
        return 'Cancelled'

    if booking.is_fully_paid():
        return 'Paid'

    if now < booking.start:
        return 'Upcoming'

    return 'Waiting taxes'