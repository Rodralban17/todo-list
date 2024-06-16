from django.test import TestCase
from .models import *
from datetime import date
from django.db import IntegrityError
# Create your tests here.
class TodoTests(TestCase):
    def setUp(self):
        self.user = User.objects.create(name='Test User', email='testuser@example.com', password='password123')
        self.task = TemdieTask.objects.create(
            title='Test Task',
            description='Test Description',
            due_date=date(2023, 12, 31),
            completed=False,
            user=self.user
        )
        self.tag1 = TemdieTag.objects.create(name='Work')
        self.tag2 = TemdieTag.objects.create(name='Personal')

    def test_task_creation(self):
        self.assertEqual(self.task.title, 'Test Task')
        self.assertEqual(self.task.description, 'Test Description')
        self.assertEqual(self.task.due_date, date(2023, 12, 31))
        self.assertFalse(self.task.completed)
        self.assertEqual(self.task.user, self.user)

    def test_task_update(self):
        self.task.title = 'Updated Task'
        self.task.completed = True
        self.task.save()
        updated_task = TemdieTask.objects.get(id=self.task.id)
        self.assertEqual(updated_task.title, 'Updated Task')
        self.assertTrue(updated_task.completed)

    def test_task_deletion(self):
        task_id = self.task.id
        self.task.delete()
        with self.assertRaises(TemdieTask.DoesNotExist):
            TemdieTask.objects.get(id=task_id)

    def test_task_status_update(self):
        self.task.completed = True
        self.task.save()
        updated_task = TemdieTask.objects.get(id=self.task.id)
        self.assertTrue(updated_task.completed)

    def test_tag_assignment(self):
        self.tag1.task.add(self.task)
        self.tag2.task.add(self.task)
        self.assertIn(self.task, self.tag1.task.all())
        self.assertIn(self.task, self.tag2.task.all())

    def test_tag_creation_and_assignment(self):
        tag = TemdieTag.objects.create(name='Urgent')
        tag.task.add(self.task)
        self.assertIn(self.task, tag.task.all())
