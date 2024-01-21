class DjobModelsConstant:
    """Константы для модели job"""
    CHAR_FIELD_MAX_LEN = 256
    INT_FIELD_MAX_VALUE = 1000000000
    INT_FIELD_MIN_VALUE = 1
    BALANCE_MAX_DIGITS = 12
    BALANCE_DECIMAL_PLACES = 2


class UserModelConstant(DjobModelsConstant):
    """Константы для модели User"""
    TEXT_FIELD_MAX_LEN = 10000
    DEFAULT_TEXT_FOR_DESCRIPTION = "Данный пользователь ничего "\
                                   "о себе не написал, " \
                                   "но мы уверены, что это очень "\
                                   "хороший и позитивный человек, " \
                                   "который скоро добьется финансовых успехов."
