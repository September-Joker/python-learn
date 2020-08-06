# 自定义过滤器
# 必要三部分：定义规则，转给python，转给url


class IntConverter:
    regex = '[0-9]+'  # 定义规则

    def to_python(self, value):
        return int(value)

    def to_url(self, value):
        return str(value)


class FourDigitYearConverter:
    regex = '[0-9]{4}'

    def to_python(self, value):
        return int(value)

    def to_url(self, value):
        return '%04d' % value
