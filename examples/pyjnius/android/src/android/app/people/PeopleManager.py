from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["PeopleManager"]

class PeopleManager(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/app/people/PeopleManager"
    addOrUpdateStatus = JavaMethod("(Ljava/lang/String;Landroid/app/people/ConversationStatus;)V")
    clearStatus = JavaMethod("(Ljava/lang/String;Ljava/lang/String;)V")
    clearStatuses = JavaMethod("(Ljava/lang/String;)V")
    getStatuses = JavaMethod("(Ljava/lang/String;)Ljava/util/List;")