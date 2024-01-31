class DjobModelsConstant:
    """Константы для модели job"""
    CHAR_FIELD_MAX_LEN = 256
    INT_FIELD_MAX_VALUE = 1000000000
    INT_FIELD_MIN_VALUE = 1
    INT_FIELD_MIN_VALUE_DURATION = 0
    BALANCE_MAX_DIGITS = 12
    BALANCE_DECIMAL_PLACES = 2
    TEXT_FIELD_MAX_LEN = 10000
    DEFAULT_TEXT_FOR_DESCRIPTION = "Дефолтное описание"
    INT_FIELD_DAY_MAX_VALUE = 30


class UserModelConstant(DjobModelsConstant):
    """Константы для модели User"""
    DEFAULT_TEXT_FOR_DESCRIPTION = "Данный пользователь ничего "\
                                   "о себе не написал, " \
                                   "но мы уверены, что это очень "\
                                   "хороший и позитивный человек, " \
                                   "который скоро добьется финансовых успехов."


class NeuralNetworkModelConstant(UserModelConstant):
    """Константы для модели Neural_network"""
    DEFAULT_TEXT_FOR_NEURAL_NETWORK = "Дефолтный текст для нейросети",
    DEFAULT_HELP_TEXT_DESCRIPTION = 'Минимум 40 символов',


class MoneyFormConstant(NeuralNetworkModelConstant):
    """Константы для формы Money"""
    HELP_TEXT_MONEY_FORM = 'Данное поле обязательное для заполнения'
    INT_FIELD_MAX_VALUE_MONEY_PERIOD = 90
    HELP_TEXT_MONEY_FORM_PERIOD = 'Указывать в днях. '\
                                  'Максимальный период - 90 дней!'
