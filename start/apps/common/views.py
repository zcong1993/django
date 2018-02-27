class ViewSetUserFilterMixin(object):
    def filter_queryset(self, queryset):
        queryset = super(ViewSetUserFilterMixin, self).filter_queryset(queryset)
        user_id = self.request.user.id
        return queryset.filter(user_id=user_id)
