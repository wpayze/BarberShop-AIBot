Enum: UserRole  
descripcion: Role of a business user.

- OWNER  
- MANAGER  
- STAFF  

Enum: BookingStatus  
descripcion: Status of a booking.

- PENDING  
- CONFIRMED  
- CANCELLED  
- NO_SHOW  

Enum: BookingSource  
descripcion: Origin of the booking.

- ONLINE  
- ADMIN_PANEL  
- WHATSAPP  
- PHONE  

Model: Business  
descripcion: A barbershop or salon using the system.

- id: uuid  
- name: string  
- slug: string  
- timezone: string  
- contactEmail: string  
- contactPhone: string  
- addressLine1: string  
- addressLine2: string  
- city: string  
- postalCode: string  
- country: string  
- planType: string  
- isActive: boolean  
- createdAt: datetime  
- updatedAt: datetime  

Model: BusinessUser  
descripcion: User that can access the backoffice for a business.

- id: uuid  
- businessId: uuid  
- email: string  
- passwordHash: string  
- role: UserRole  
- isActive: boolean  
- createdAt: datetime  
- updatedAt: datetime  

Model: Staff  
descripcion: A barber or stylist working at a business.

- id: uuid  
- businessId: uuid  
- displayName: string  
- photoUrl: string  
- bio: string  
- isActive: boolean  
- sortOrder: integer  
- createdAt: datetime  
- updatedAt: datetime  

Model: Service  
descripcion: A bookable service.

- id: uuid  
- businessId: uuid  
- name: string  
- description: string  
- durationMinutes: integer  
- price: decimal  
- category: string  
- isActive: boolean  
- createdAt: datetime  
- updatedAt: datetime  

Model: StaffService  
descripcion: Links which staff can perform which services.

- id: uuid  
- staffId: uuid  
- serviceId: uuid  
- createdAt: datetime  
- (unique: staffId + serviceId)  

Model: BusinessOpeningHours  
descripcion: Weekly opening hours for a business.

- id: uuid  
- businessId: uuid  
- dayOfWeek: integer  
- openTime: time  
- closeTime: time  
- isClosed: boolean  

Model: StaffScheduleOverride  
descripcion: Special schedule or day off for a staff member.

- id: uuid  
- staffId: uuid  
- date: date  
- isDayOff: boolean  
- startTime: time  
- endTime: time  

Model: Client  
descripcion: End customer of a business.

- id: uuid  
- businessId: uuid  
- fullName: string  
- phone: string  
- email: string  
- notes: string  
- createdAt: datetime  
- updatedAt: datetime  

Model: Booking  
descripcion: A booking for a service, staff and time slot.

- id: uuid  
- businessId: uuid  
- staffId: uuid  
- serviceId: uuid  
- clientId: uuid  
- clientName: string  
- clientPhone: string  
- clientEmail: string  
- date: date  
- startTime: time  
- endTime: time  
- status: BookingStatus  
- source: BookingSource  
- notes: string  
- createdAt: datetime  
- updatedAt: datetime  

Model: NotificationLog  
descripcion: Log of notification attempts.

- id: uuid  
- businessId: uuid  
- bookingId: uuid  
- channel: string  
- recipient: string  
- templateKey: string  
- payload: json  
- status: string  
- errorMessage: string  
- createdAt: datetime  
