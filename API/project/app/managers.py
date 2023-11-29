from .models import Pereval, Image

class PerevalManager:
    @staticmethod
    def submit_data(data):
        try:
            user_data = data.get('user', {})
            coords_data = data.get('coords', {})
            level_data = data.get('level', {})
            images_data = data.get('images', [])

            pereval = Pereval.objects.create(
                beauty_title=data.get('beauty_title', ''),
                title=data.get('title', ''),
                other_titles=data.get('other_titles', ''),
                connect=data.get('connect', ''),
                add_time=data.get('add_time', ''),
                user_email=user_data.get('email', ''),
                user_fam=user_data.get('fam', ''),
                user_name=user_data.get('name', ''),
                user_otc=user_data.get('otc', ''),
                user_phone=user_data.get('phone', ''),
                latitude=coords_data.get('latitude', ''),
                longitude=coords_data.get('longitude', ''),
                height=coords_data.get('height', ''),
                winter_level=level_data.get('winter', ''),
                summer_level=level_data.get('summer', ''),
                autumn_level=level_data.get('autumn', ''),
                spring_level=level_data.get('spring', ''),
            )

            for image_data in images_data:
                Image.objects.create(
                    pereval=pereval,
                    data=image_data.get('data', ''),
                    title=image_data.get('title', ''),
                )

            return {'status': 200, 'message': 'Отправлено успешно', 'id': pereval.id}
        except Exception:
            return {'status': 500, 'message': 'Ошибка подключения к базе данных', 'id': None}
