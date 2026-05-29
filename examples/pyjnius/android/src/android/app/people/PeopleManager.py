from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["PeopleManager"]

class PeopleManager(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/app/people/PeopleManager"
    getStatuses = JavaMethod("(Ljava/lang/String;)Ljava/util/List;")
    clearStatuses = JavaMethod("(Ljava/lang/String;)V")
    addOrUpdateStatus = JavaMethod("(Ljava/lang/String;Landroid/app/people/ConversationStatus;)V")
    clearStatus = JavaMethod("(Ljava/lang/String;Ljava/lang/String;)V")