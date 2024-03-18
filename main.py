import random
import asyncio


def CreateSuperUser(username, password, bio, birthday):
    user = User(username = username,
                        birthday = birthday,
                        bio = bio,
                        is_staff = True,
                        is_superuser = True)
    user.set_password(password)
    user.save()


def generate_user(number: int):
    for _ in range(number):
        user = User.objects.create(username = fake.name(),
                                #    password = fake.password()
                                   birthday = fake.date(),
                                   bio = fake.text())
        user.set_password(fake.password())
        print(user)

def generate_post(number: int):
    for _ in range(number):
        post = Post.objects.create(title = fake.address(),
                                body = fake.text(),
                                is_active = random.choice([True, False]),
                                authors = random.choice(User.objects.all()))
        print(post.authors, post.title)


def generate_like(number: int):
    for _ in range(number):
        like = Like.objects.create(
            authors = random.choice(User.objects.all()),
            posts = random.choice(Post.objects.all())
        )
        print(like)


def generate_comment(number: int):
    for _ in range(number):
        comment = Comment.objects.create(
            body = fake.text(),
            authors = random.choice(User.objects.all()),
            posts = random.choice(Post.objects.all())
        )
        print(comment)


async def main():
    # await asyncio.gather(
    #     generate_user(2),
    #     generate_post(4),
    #     generate_like(16),
    #     generate_comment(8),
    # )
    # loop = asyncio.get_event_loop()
    # task1 = loop.create_task(generate_user(3))
    
    pass



if __name__ == '__main__':
    import os

    from django.core.asgi import get_asgi_application

    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')

    application = get_asgi_application()
    from Api.models import User, Post, Comment, Like
    import faker

    fake = faker.Faker()

    asyncio.run(main())
