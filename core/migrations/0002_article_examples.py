from django.db import migrations


def create_articles(apps, schema_editor):
    Article = apps.get_model("core", "Article")
    Article.objects.create(
        title="IA Generativa: Transformando a Indústria Criativa",
        content=(
            "Ferramentas como ChatGPT e DALL-E estão revolucionando áreas como "
            "design, redação e produção audiovisual, permitindo automação e "
            "novas formas de expressão."
        ),
    )
    Article.objects.create(
        title="Desafios Éticos na Inteligência Artificial",
        content=(
            "Discussões sobre viés algorítmico, privacidade e impacto social "
            "estão cada vez mais presentes, exigindo regulamentação e "
            "transparência das empresas de tecnologia."
        ),
    )
    Article.objects.create(
        title="IA na Saúde: Diagnóstico e Prevenção",
        content=(
            "Soluções baseadas em IA estão auxiliando médicos no diagnóstico "
            "precoce de doenças, análise de exames e personalização de "
            "tratamentos, melhorando a eficiência do setor."
        ),
    )


class Migration(migrations.Migration):
    dependencies = [
        ("core", "0001_initial"),
    ]

    operations = [
        migrations.RunPython(create_articles),
    ]
