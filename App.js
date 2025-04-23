import React, { useEffect, useState } from 'react';
import { Input } from '@/components/ui/input'; // Замените на стандартный Input, если нет этого компонента
import { Button } from '@/components/ui/button'; // Замените на стандартную кнопку, если нет этого компонента
import { Card, CardContent } from '@/components/ui/card'; // Замените на стандартные карточки
import { Progress } from '@/components/ui/progress'; // Замените на стандартный Progress, если нет этого компонента

const goals = {
  'Похудение': 1200,
  'Поддержание': 2000,
  'Набор массы': 2800
};

const questions = [
  {
    question: 'Какой у вас уровень физической активности?',
    options: [
      { text: 'Минимальный', goal: 'Похудение' },
      { text: 'Средний', goal: 'Поддержание' },
      { text: 'Высокий', goal: 'Набор массы' }
    ]
  },
  {
    question: 'Какова ваша основная цель питания?',
    options: [
      { text: 'Снижение веса', goal: 'Похудение' },
      { text: 'Стабильное питание', goal: 'Поддержание' },
      { text: 'Рост мышечной массы', goal: 'Набор массы' }
    ]
  },
  {
    question: 'Какой у вас тип телосложения?',
    options: [
      { text: 'Эктоморф', goal: 'Набор массы' },
      { text: 'Мезоморф', goal: 'Поддержание' },
      { text: 'Эндоморф', goal: 'Похудение' }
    ]
  }
];

export default function MainPage() {
  const [isLoggedIn, setIsLoggedIn] = useState(false);
  const [username, setUsername] = useState('');
  const [password, setPassword] = useState('');
  const [isRegistering, setIsRegistering] = useState(false);
  const [goal, setGoal] = useState('');
  const [step, setStep] = useState('auth');
  const [meals, setMeals] = useState({
    Завтрак: [],
    Обед: [],
    Ужин: [],
    Перекус: []
  });
  const [selectedMeal, setSelectedMeal] = useState('Завтрак');
  const [newProduct, setNewProduct] = useState('');
  const [grams, setGrams] = useState('');
  const [questionIndex, setQuestionIndex] = useState(0);
  const [goalVotes, setGoalVotes] = useState({ 'Похудение': 0, 'Поддержание': 0, 'Набор массы': 0 });

  const totalCalories = Object.values(meals).flat().reduce((sum, p) => sum + p.calories, 0);

  useEffect(() => {
    const storedUser = localStorage.getItem('username');
    const storedMeals = localStorage.getItem('meals');
    const storedGoal = localStorage.getItem('goal');
    if (storedUser) {
      setIsLoggedIn(true);
      if (storedMeals) setMeals(JSON.parse(storedMeals));
      if (storedGoal) setGoal(storedGoal);
      if (!storedGoal) setStep('test');
      else setStep('main');
    }
  }, []);

  useEffect(() => {
    localStorage.setItem('meals', JSON.stringify(meals));
  }, [meals]);

  useEffect(() => {
    if (goal) localStorage.setItem('goal', goal);
  }, [goal]);

  const handleAuth = () => {
    if (username && password) {
      localStorage.setItem('username', username);
      setIsLoggedIn(true);
      setStep('test');
    }
  };

  const handleLogout = () => {
    if (confirm('Вы уверены, что хотите выйти?')) {
      localStorage.removeItem('username');
      localStorage.removeItem('meals');
      localStorage.removeItem('goal');
      setIsLoggedIn(false);
      setUsername('');
      setPassword('');
      setGoal('');
      setMeals({ Завтрак: [], Обед: [], Ужин: [], Перекус: [] });
      setStep('auth');
    }
  };

  const addProduct = () => {
    if (newProduct && grams) {
      const updatedMeal = [...meals[selectedMeal], {
        name: newProduct,
        grams: parseInt(grams),
        calories: Math.round(Math.random() * 500),
      }];
      setMeals({ ...meals, [selectedMeal]: updatedMeal });
      setNewProduct('');
      setGrams('');
    }
  };

  const handleAnswer = (selectedGoal) => {
    const updatedVotes = { ...goalVotes, [selectedGoal]: goalVotes[selectedGoal] + 1 };
    setGoalVotes(updatedVotes);
    if (questionIndex + 1 < questions.length) {
      setQuestionIndex(questionIndex + 1);
    } else {
      const finalGoal = Object.entries(updatedVotes).reduce((a, b) => (a[1] > b[1] ? a : b))[0];
      setGoal(finalGoal);
      setStep('main');
    }
  };

  if (!isLoggedIn) {
    return (
      <div className="p-4 max-w-sm mx-auto mt-20">
        <h2 className="text-2xl font-bold mb-4">{isRegistering ? 'Регистрация' : 'Авторизация'}</h2>
        <Input placeholder="Логин" value={username} onChange={(e) => setUsername(e.target.value)} className="mb-2" />
        <Input placeholder="Пароль" type="password" value={password} onChange={(e) => setPassword(e.target.value)} className="mb-4" />
        <Button onClick={handleAuth}>{isRegistering ? 'Зарегистрироваться' : 'Войти'}</Button>
        <Button variant="link" onClick={() => setIsRegistering(!isRegistering)} className="mt-2">
          {isRegistering ? 'Уже есть аккаунт?' : 'Нет аккаунта? Зарегистрироваться'}
        </Button>
      </div>
    );
  }

  if (step === 'test') {
    const currentQuestion = questions[questionIndex];
    return (
      <div className="p-4 max-w-md mx-auto mt-20 space-y-4">
        <h2 className="text-2xl font-bold">{currentQuestion.question}</h2>
        <div className="space-y-2">
          {currentQuestion.options.map((opt, idx) => (
            <Button key={idx} className="w-full" onClick={() => handleAnswer(opt.goal)}>{opt.text}</Button>
          ))}
        </div>
      </div>
    );
  }

  return (
    <div className="p-4 max-w-3xl mx-auto">
      <div className="flex justify-between items-center mb-4">
        <h1 className="text-3xl font-bold">ГЛАВНАЯ</h1>
        <Button variant="outline" onClick={handleLogout}>Выйти</Button>
      </div>
      <p className="mb-2">Цель: {goal}</p>
      <div className="mb-4">
        <Progress value={(totalCalories / goals[goal]) * 100} />
        <div className="text-sm text-muted-foreground">{totalCalories} ккал из {goals[goal]}</div>
      </div>

      <div className="flex gap-2 mb-4">
        {Object.keys(meals).map((meal) => (
          <Button key={meal} variant={meal === selectedMeal ? 'default' : 'outline'} onClick={() => setSelectedMeal(meal)}>
            {meal}
          </Button>
        ))}
      </div>

      <Card className="mb-4">
        <CardContent className="p-4 space-y-2">
          <h2 className="text-xl font-semibold">{selectedMeal}</h2>
          {meals[selectedMeal].map((p, index) => (
            <div key={index} className="flex justify-between">
              <span>{p.name}</span>
              <span>{p.grams} г</span>
            </div>
          ))}
          <div className="flex gap-2">
            <Input placeholder="Продукт" value={newProduct} onChange={(e) => setNewProduct(e.target.value)} />
            <Input placeholder="Грамм" type="number" value={grams} onChange={(e) => setGrams(e.target.value)} />
            <Button onClick={addProduct}>+</Button>
          </div>
        </CardContent>
      </Card>

      <Card>
        <CardContent className="p-4">
          <p>Витамины и минералы в еде:</p>
          <ul className="list-disc ml-5 text-sm">
            <li>Витамин A</li>
            <li>Витамин C</li>
            <li>Кальций</li>
            <li>Железо</li>
          </ul>
        </CardContent>
      </Card>
    </div>
  );
}
