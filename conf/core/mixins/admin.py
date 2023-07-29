import csv
from datetime import datetime

from django.http import HttpResponse


class ExportCsvMixin:
    @classmethod
    def get_field_names(cls) -> list:
        # meta = self.model._meta
        """ Refer to comment on line 34"""
        # field_names = [field.name for field in meta.fields]
        raise NotImplementedError

    @classmethod
    def get_query_data(cls):
        """ Commented this out to handle the logic better for making this export feature more generic"""
        # for obj in queryset:
        #     row = writer.writerow([getattr(obj, field) for field in field_names])
        raise NotImplementedError

    def export_as_csv(self, request, queryset):
        field_names = self.get_field_names()

        response = HttpResponse(content_type='text/csv')
        response['Content-Disposition'] = 'attachment; filename=File-{}.csv'.format(datetime.now())
        writer = csv.writer(response)

        writer.writerow(field_names)

        query_result = self.get_query_data()
        for item in query_result:
            writer.writerow(item)

        return response

    export_as_csv.short_description = "Export as Csv"
