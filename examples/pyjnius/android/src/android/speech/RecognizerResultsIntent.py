from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["RecognizerResultsIntent"]

class RecognizerResultsIntent(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/speech/RecognizerResultsIntent"
    ACTION_VOICE_SEARCH_RESULTS = JavaStaticField("Ljava/lang/String;")
    EXTRA_VOICE_SEARCH_RESULT_HTML = JavaStaticField("Ljava/lang/String;")
    EXTRA_VOICE_SEARCH_RESULT_HTML_BASE_URLS = JavaStaticField("Ljava/lang/String;")
    EXTRA_VOICE_SEARCH_RESULT_HTTP_HEADERS = JavaStaticField("Ljava/lang/String;")
    EXTRA_VOICE_SEARCH_RESULT_STRINGS = JavaStaticField("Ljava/lang/String;")
    EXTRA_VOICE_SEARCH_RESULT_URLS = JavaStaticField("Ljava/lang/String;")
    URI_SCHEME_INLINE = JavaStaticField("Ljava/lang/String;")