from fastapi import HTTPException, status, Response, Depends

UserAlreadyExistsException = HTTPException(
  status_code=status.HTTP_409_CONFLICT,
  detail="Пользователь уже существует"
)
IncorrectEmailOrPasswordException = HTTPException(
  status_code= status.HTTP_401_UNAUTHORIZED,
  detail="Неверная почта или пароль")
TokenExpiredException = HTTPException(
  status_code= status.HTTP_401_UNAUTHORIZED,
  detail="Токен истёк")

TokenAbsentException = HTTPException(
  status_code= status.HTTP_401_UNAUTHORIZED,
  detail="Токен отсутствует")

IncorrectTokenFormatException = HTTPException(
  status_code= status.HTTP_401_UNAUTHORIZED,
  detail="Неверный формат токена")

UserIsNotPresentException = HTTPException(
  status_code= status.HTTP_401_UNAUTHORIZED)

EventAbsenceException = HTTPException(
  status_code=status.HTTP_404_NOT_FOUND,
  detail="Такого мероприятия не существует"
)
EventFullException = HTTPException(
  status_code=status.HTTP_409_CONFLICT,
  detail="Все места на это событие уже заняты"
)
EventAlreadyBookedException = HTTPException(
  status_code=status.HTTP_409_CONFLICT,
  detail="Вы уже забронировали место на этом мероприятии"
)
UserEventAbsenceException = HTTPException(
  status_code=status.HTTP_404_NOT_FOUND,
  detail="Мероприятия нет в забронированных"
)
