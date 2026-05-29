from typing import Any, ClassVar, overload
from java.nio.ByteBuffer import ByteBuffer
from java.nio.IntBuffer import IntBuffer

class GLES31Ext:
    GL_BLEND_ADVANCED_COHERENT_KHR: ClassVar[int]
    GL_BUFFER_KHR: ClassVar[int]
    GL_CLAMP_TO_BORDER_EXT: ClassVar[int]
    GL_COLORBURN_KHR: ClassVar[int]
    GL_COLORDODGE_KHR: ClassVar[int]
    GL_COMPRESSED_RGBA_ASTC_10x10_KHR: ClassVar[int]
    GL_COMPRESSED_RGBA_ASTC_10x5_KHR: ClassVar[int]
    GL_COMPRESSED_RGBA_ASTC_10x6_KHR: ClassVar[int]
    GL_COMPRESSED_RGBA_ASTC_10x8_KHR: ClassVar[int]
    GL_COMPRESSED_RGBA_ASTC_12x10_KHR: ClassVar[int]
    GL_COMPRESSED_RGBA_ASTC_12x12_KHR: ClassVar[int]
    GL_COMPRESSED_RGBA_ASTC_4x4_KHR: ClassVar[int]
    GL_COMPRESSED_RGBA_ASTC_5x4_KHR: ClassVar[int]
    GL_COMPRESSED_RGBA_ASTC_5x5_KHR: ClassVar[int]
    GL_COMPRESSED_RGBA_ASTC_6x5_KHR: ClassVar[int]
    GL_COMPRESSED_RGBA_ASTC_6x6_KHR: ClassVar[int]
    GL_COMPRESSED_RGBA_ASTC_8x5_KHR: ClassVar[int]
    GL_COMPRESSED_RGBA_ASTC_8x6_KHR: ClassVar[int]
    GL_COMPRESSED_RGBA_ASTC_8x8_KHR: ClassVar[int]
    GL_COMPRESSED_SRGB8_ALPHA8_ASTC_10x10_KHR: ClassVar[int]
    GL_COMPRESSED_SRGB8_ALPHA8_ASTC_10x5_KHR: ClassVar[int]
    GL_COMPRESSED_SRGB8_ALPHA8_ASTC_10x6_KHR: ClassVar[int]
    GL_COMPRESSED_SRGB8_ALPHA8_ASTC_10x8_KHR: ClassVar[int]
    GL_COMPRESSED_SRGB8_ALPHA8_ASTC_12x10_KHR: ClassVar[int]
    GL_COMPRESSED_SRGB8_ALPHA8_ASTC_12x12_KHR: ClassVar[int]
    GL_COMPRESSED_SRGB8_ALPHA8_ASTC_4x4_KHR: ClassVar[int]
    GL_COMPRESSED_SRGB8_ALPHA8_ASTC_5x4_KHR: ClassVar[int]
    GL_COMPRESSED_SRGB8_ALPHA8_ASTC_5x5_KHR: ClassVar[int]
    GL_COMPRESSED_SRGB8_ALPHA8_ASTC_6x5_KHR: ClassVar[int]
    GL_COMPRESSED_SRGB8_ALPHA8_ASTC_6x6_KHR: ClassVar[int]
    GL_COMPRESSED_SRGB8_ALPHA8_ASTC_8x5_KHR: ClassVar[int]
    GL_COMPRESSED_SRGB8_ALPHA8_ASTC_8x6_KHR: ClassVar[int]
    GL_COMPRESSED_SRGB8_ALPHA8_ASTC_8x8_KHR: ClassVar[int]
    GL_CONTEXT_FLAG_DEBUG_BIT_KHR: ClassVar[int]
    GL_DARKEN_KHR: ClassVar[int]
    GL_DEBUG_CALLBACK_FUNCTION_KHR: ClassVar[int]
    GL_DEBUG_CALLBACK_USER_PARAM_KHR: ClassVar[int]
    GL_DEBUG_GROUP_STACK_DEPTH_KHR: ClassVar[int]
    GL_DEBUG_LOGGED_MESSAGES_KHR: ClassVar[int]
    GL_DEBUG_NEXT_LOGGED_MESSAGE_LENGTH_KHR: ClassVar[int]
    GL_DEBUG_OUTPUT_KHR: ClassVar[int]
    GL_DEBUG_OUTPUT_SYNCHRONOUS_KHR: ClassVar[int]
    GL_DEBUG_SEVERITY_HIGH_KHR: ClassVar[int]
    GL_DEBUG_SEVERITY_LOW_KHR: ClassVar[int]
    GL_DEBUG_SEVERITY_MEDIUM_KHR: ClassVar[int]
    GL_DEBUG_SEVERITY_NOTIFICATION_KHR: ClassVar[int]
    GL_DEBUG_SOURCE_API_KHR: ClassVar[int]
    GL_DEBUG_SOURCE_APPLICATION_KHR: ClassVar[int]
    GL_DEBUG_SOURCE_OTHER_KHR: ClassVar[int]
    GL_DEBUG_SOURCE_SHADER_COMPILER_KHR: ClassVar[int]
    GL_DEBUG_SOURCE_THIRD_PARTY_KHR: ClassVar[int]
    GL_DEBUG_SOURCE_WINDOW_SYSTEM_KHR: ClassVar[int]
    GL_DEBUG_TYPE_DEPRECATED_BEHAVIOR_KHR: ClassVar[int]
    GL_DEBUG_TYPE_ERROR_KHR: ClassVar[int]
    GL_DEBUG_TYPE_MARKER_KHR: ClassVar[int]
    GL_DEBUG_TYPE_OTHER_KHR: ClassVar[int]
    GL_DEBUG_TYPE_PERFORMANCE_KHR: ClassVar[int]
    GL_DEBUG_TYPE_POP_GROUP_KHR: ClassVar[int]
    GL_DEBUG_TYPE_PORTABILITY_KHR: ClassVar[int]
    GL_DEBUG_TYPE_PUSH_GROUP_KHR: ClassVar[int]
    GL_DEBUG_TYPE_UNDEFINED_BEHAVIOR_KHR: ClassVar[int]
    GL_DECODE_EXT: ClassVar[int]
    GL_DIFFERENCE_KHR: ClassVar[int]
    GL_EXCLUSION_KHR: ClassVar[int]
    GL_FIRST_VERTEX_CONVENTION_EXT: ClassVar[int]
    GL_FRACTIONAL_EVEN_EXT: ClassVar[int]
    GL_FRACTIONAL_ODD_EXT: ClassVar[int]
    GL_FRAGMENT_INTERPOLATION_OFFSET_BITS_OES: ClassVar[int]
    GL_FRAMEBUFFER_ATTACHMENT_LAYERED_EXT: ClassVar[int]
    GL_FRAMEBUFFER_DEFAULT_LAYERS_EXT: ClassVar[int]
    GL_FRAMEBUFFER_INCOMPLETE_LAYER_TARGETS_EXT: ClassVar[int]
    GL_GEOMETRY_LINKED_INPUT_TYPE_EXT: ClassVar[int]
    GL_GEOMETRY_LINKED_OUTPUT_TYPE_EXT: ClassVar[int]
    GL_GEOMETRY_LINKED_VERTICES_OUT_EXT: ClassVar[int]
    GL_GEOMETRY_SHADER_BIT_EXT: ClassVar[int]
    GL_GEOMETRY_SHADER_EXT: ClassVar[int]
    GL_GEOMETRY_SHADER_INVOCATIONS_EXT: ClassVar[int]
    GL_HARDLIGHT_KHR: ClassVar[int]
    GL_HSL_COLOR_KHR: ClassVar[int]
    GL_HSL_HUE_KHR: ClassVar[int]
    GL_HSL_LUMINOSITY_KHR: ClassVar[int]
    GL_HSL_SATURATION_KHR: ClassVar[int]
    GL_IMAGE_BUFFER_EXT: ClassVar[int]
    GL_IMAGE_CUBE_MAP_ARRAY_EXT: ClassVar[int]
    GL_INT_IMAGE_BUFFER_EXT: ClassVar[int]
    GL_INT_IMAGE_CUBE_MAP_ARRAY_EXT: ClassVar[int]
    GL_INT_SAMPLER_2D_MULTISAMPLE_ARRAY_OES: ClassVar[int]
    GL_INT_SAMPLER_BUFFER_EXT: ClassVar[int]
    GL_INT_SAMPLER_CUBE_MAP_ARRAY_EXT: ClassVar[int]
    GL_ISOLINES_EXT: ClassVar[int]
    GL_IS_PER_PATCH_EXT: ClassVar[int]
    GL_LAST_VERTEX_CONVENTION_EXT: ClassVar[int]
    GL_LAYER_PROVOKING_VERTEX_EXT: ClassVar[int]
    GL_LIGHTEN_KHR: ClassVar[int]
    GL_LINES_ADJACENCY_EXT: ClassVar[int]
    GL_LINE_STRIP_ADJACENCY_EXT: ClassVar[int]
    GL_MAX_COMBINED_GEOMETRY_UNIFORM_COMPONENTS_EXT: ClassVar[int]
    GL_MAX_COMBINED_TESS_CONTROL_UNIFORM_COMPONENTS_EXT: ClassVar[int]
    GL_MAX_COMBINED_TESS_EVALUATION_UNIFORM_COMPONENTS_EXT: ClassVar[int]
    GL_MAX_DEBUG_GROUP_STACK_DEPTH_KHR: ClassVar[int]
    GL_MAX_DEBUG_LOGGED_MESSAGES_KHR: ClassVar[int]
    GL_MAX_DEBUG_MESSAGE_LENGTH_KHR: ClassVar[int]
    GL_MAX_FRAGMENT_INTERPOLATION_OFFSET_OES: ClassVar[int]
    GL_MAX_FRAMEBUFFER_LAYERS_EXT: ClassVar[int]
    GL_MAX_GEOMETRY_ATOMIC_COUNTERS_EXT: ClassVar[int]
    GL_MAX_GEOMETRY_ATOMIC_COUNTER_BUFFERS_EXT: ClassVar[int]
    GL_MAX_GEOMETRY_IMAGE_UNIFORMS_EXT: ClassVar[int]
    GL_MAX_GEOMETRY_INPUT_COMPONENTS_EXT: ClassVar[int]
    GL_MAX_GEOMETRY_OUTPUT_COMPONENTS_EXT: ClassVar[int]
    GL_MAX_GEOMETRY_OUTPUT_VERTICES_EXT: ClassVar[int]
    GL_MAX_GEOMETRY_SHADER_INVOCATIONS_EXT: ClassVar[int]
    GL_MAX_GEOMETRY_SHADER_STORAGE_BLOCKS_EXT: ClassVar[int]
    GL_MAX_GEOMETRY_TEXTURE_IMAGE_UNITS_EXT: ClassVar[int]
    GL_MAX_GEOMETRY_TOTAL_OUTPUT_COMPONENTS_EXT: ClassVar[int]
    GL_MAX_GEOMETRY_UNIFORM_BLOCKS_EXT: ClassVar[int]
    GL_MAX_GEOMETRY_UNIFORM_COMPONENTS_EXT: ClassVar[int]
    GL_MAX_LABEL_LENGTH_KHR: ClassVar[int]
    GL_MAX_PATCH_VERTICES_EXT: ClassVar[int]
    GL_MAX_TESS_CONTROL_ATOMIC_COUNTERS_EXT: ClassVar[int]
    GL_MAX_TESS_CONTROL_ATOMIC_COUNTER_BUFFERS_EXT: ClassVar[int]
    GL_MAX_TESS_CONTROL_IMAGE_UNIFORMS_EXT: ClassVar[int]
    GL_MAX_TESS_CONTROL_INPUT_COMPONENTS_EXT: ClassVar[int]
    GL_MAX_TESS_CONTROL_OUTPUT_COMPONENTS_EXT: ClassVar[int]
    GL_MAX_TESS_CONTROL_SHADER_STORAGE_BLOCKS_EXT: ClassVar[int]
    GL_MAX_TESS_CONTROL_TEXTURE_IMAGE_UNITS_EXT: ClassVar[int]
    GL_MAX_TESS_CONTROL_TOTAL_OUTPUT_COMPONENTS_EXT: ClassVar[int]
    GL_MAX_TESS_CONTROL_UNIFORM_BLOCKS_EXT: ClassVar[int]
    GL_MAX_TESS_CONTROL_UNIFORM_COMPONENTS_EXT: ClassVar[int]
    GL_MAX_TESS_EVALUATION_ATOMIC_COUNTERS_EXT: ClassVar[int]
    GL_MAX_TESS_EVALUATION_ATOMIC_COUNTER_BUFFERS_EXT: ClassVar[int]
    GL_MAX_TESS_EVALUATION_IMAGE_UNIFORMS_EXT: ClassVar[int]
    GL_MAX_TESS_EVALUATION_INPUT_COMPONENTS_EXT: ClassVar[int]
    GL_MAX_TESS_EVALUATION_OUTPUT_COMPONENTS_EXT: ClassVar[int]
    GL_MAX_TESS_EVALUATION_SHADER_STORAGE_BLOCKS_EXT: ClassVar[int]
    GL_MAX_TESS_EVALUATION_TEXTURE_IMAGE_UNITS_EXT: ClassVar[int]
    GL_MAX_TESS_EVALUATION_UNIFORM_BLOCKS_EXT: ClassVar[int]
    GL_MAX_TESS_EVALUATION_UNIFORM_COMPONENTS_EXT: ClassVar[int]
    GL_MAX_TESS_GEN_LEVEL_EXT: ClassVar[int]
    GL_MAX_TESS_PATCH_COMPONENTS_EXT: ClassVar[int]
    GL_MAX_TEXTURE_BUFFER_SIZE_EXT: ClassVar[int]
    GL_MIN_FRAGMENT_INTERPOLATION_OFFSET_OES: ClassVar[int]
    GL_MIN_SAMPLE_SHADING_VALUE_OES: ClassVar[int]
    GL_MULTIPLY_KHR: ClassVar[int]
    GL_OVERLAY_KHR: ClassVar[int]
    GL_PATCHES_EXT: ClassVar[int]
    GL_PATCH_VERTICES_EXT: ClassVar[int]
    GL_PRIMITIVES_GENERATED_EXT: ClassVar[int]
    GL_PRIMITIVE_BOUNDING_BOX_EXT: ClassVar[int]
    GL_PRIMITIVE_RESTART_FOR_PATCHES_SUPPORTED: ClassVar[int]
    GL_PROGRAM_KHR: ClassVar[int]
    GL_QUADS_EXT: ClassVar[int]
    GL_QUERY_KHR: ClassVar[int]
    GL_REFERENCED_BY_GEOMETRY_SHADER_EXT: ClassVar[int]
    GL_REFERENCED_BY_TESS_CONTROL_SHADER_EXT: ClassVar[int]
    GL_REFERENCED_BY_TESS_EVALUATION_SHADER_EXT: ClassVar[int]
    GL_SAMPLER_2D_MULTISAMPLE_ARRAY_OES: ClassVar[int]
    GL_SAMPLER_BUFFER_EXT: ClassVar[int]
    GL_SAMPLER_CUBE_MAP_ARRAY_EXT: ClassVar[int]
    GL_SAMPLER_CUBE_MAP_ARRAY_SHADOW_EXT: ClassVar[int]
    GL_SAMPLER_KHR: ClassVar[int]
    GL_SAMPLE_SHADING_OES: ClassVar[int]
    GL_SCREEN_KHR: ClassVar[int]
    GL_SHADER_KHR: ClassVar[int]
    GL_SKIP_DECODE_EXT: ClassVar[int]
    GL_SOFTLIGHT_KHR: ClassVar[int]
    GL_STACK_OVERFLOW_KHR: ClassVar[int]
    GL_STACK_UNDERFLOW_KHR: ClassVar[int]
    GL_STENCIL_INDEX8_OES: ClassVar[int]
    GL_STENCIL_INDEX_OES: ClassVar[int]
    GL_TESS_CONTROL_OUTPUT_VERTICES_EXT: ClassVar[int]
    GL_TESS_CONTROL_SHADER_BIT_EXT: ClassVar[int]
    GL_TESS_CONTROL_SHADER_EXT: ClassVar[int]
    GL_TESS_EVALUATION_SHADER_BIT_EXT: ClassVar[int]
    GL_TESS_EVALUATION_SHADER_EXT: ClassVar[int]
    GL_TESS_GEN_MODE_EXT: ClassVar[int]
    GL_TESS_GEN_POINT_MODE_EXT: ClassVar[int]
    GL_TESS_GEN_SPACING_EXT: ClassVar[int]
    GL_TESS_GEN_VERTEX_ORDER_EXT: ClassVar[int]
    GL_TEXTURE_2D_MULTISAMPLE_ARRAY_OES: ClassVar[int]
    GL_TEXTURE_BINDING_2D_MULTISAMPLE_ARRAY_OES: ClassVar[int]
    GL_TEXTURE_BINDING_BUFFER_EXT: ClassVar[int]
    GL_TEXTURE_BINDING_CUBE_MAP_ARRAY_EXT: ClassVar[int]
    GL_TEXTURE_BORDER_COLOR_EXT: ClassVar[int]
    GL_TEXTURE_BUFFER_BINDING_EXT: ClassVar[int]
    GL_TEXTURE_BUFFER_DATA_STORE_BINDING_EXT: ClassVar[int]
    GL_TEXTURE_BUFFER_EXT: ClassVar[int]
    GL_TEXTURE_BUFFER_OFFSET_ALIGNMENT_EXT: ClassVar[int]
    GL_TEXTURE_BUFFER_OFFSET_EXT: ClassVar[int]
    GL_TEXTURE_BUFFER_SIZE_EXT: ClassVar[int]
    GL_TEXTURE_CUBE_MAP_ARRAY_EXT: ClassVar[int]
    GL_TEXTURE_SRGB_DECODE_EXT: ClassVar[int]
    GL_TRIANGLES_ADJACENCY_EXT: ClassVar[int]
    GL_TRIANGLE_STRIP_ADJACENCY_EXT: ClassVar[int]
    GL_UNDEFINED_VERTEX_EXT: ClassVar[int]
    GL_UNSIGNED_INT_IMAGE_BUFFER_EXT: ClassVar[int]
    GL_UNSIGNED_INT_IMAGE_CUBE_MAP_ARRAY_EXT: ClassVar[int]
    GL_UNSIGNED_INT_SAMPLER_2D_MULTISAMPLE_ARRAY_OES: ClassVar[int]
    GL_UNSIGNED_INT_SAMPLER_BUFFER_EXT: ClassVar[int]
    GL_UNSIGNED_INT_SAMPLER_CUBE_MAP_ARRAY_EXT: ClassVar[int]
    GL_VERTEX_ARRAY_KHR: ClassVar[int]
    @staticmethod
    def glBlendBarrierKHR() -> None: ...
    @staticmethod
    def glBlendEquationSeparateiEXT(p0: int, p1: int, p2: int) -> None: ...
    @staticmethod
    def glBlendEquationiEXT(p0: int, p1: int) -> None: ...
    @staticmethod
    def glBlendFuncSeparateiEXT(p0: int, p1: int, p2: int, p3: int, p4: int) -> None: ...
    @staticmethod
    def glBlendFunciEXT(p0: int, p1: int, p2: int) -> None: ...
    @staticmethod
    def glColorMaskiEXT(p0: int, p1: bool, p2: bool, p3: bool, p4: bool) -> None: ...
    @staticmethod
    def glCopyImageSubDataEXT(p0: int, p1: int, p2: int, p3: int, p4: int, p5: int, p6: int, p7: int, p8: int, p9: int, p10: int, p11: int, p12: int, p13: int, p14: int) -> None: ...
    @staticmethod
    def glDebugMessageCallbackKHR(p0: Any) -> None: ...
    @overload
    @staticmethod
    def glDebugMessageControlKHR(p0: int, p1: int, p2: int, p3: int, p4: Any, p5: int, p6: bool) -> None: ...
    @overload
    @staticmethod
    def glDebugMessageControlKHR(p0: int, p1: int, p2: int, p3: int, p4: IntBuffer, p5: bool) -> None: ...
    @staticmethod
    def glDebugMessageInsertKHR(p0: int, p1: int, p2: int, p3: int, p4: str) -> None: ...
    @staticmethod
    def glDisableiEXT(p0: int, p1: int) -> None: ...
    @staticmethod
    def glEnableiEXT(p0: int, p1: int) -> None: ...
    @staticmethod
    def glFramebufferTextureEXT(p0: int, p1: int, p2: int, p3: int) -> None: ...
    @staticmethod
    def glGetDebugMessageCallbackKHR() -> Any: ...
    @overload
    @staticmethod
    def glGetDebugMessageLogKHR(p0: int, p1: IntBuffer, p2: IntBuffer, p3: IntBuffer, p4: IntBuffer) -> Any: ...
    @overload
    @staticmethod
    def glGetDebugMessageLogKHR(p0: int, p1: IntBuffer, p2: IntBuffer, p3: IntBuffer, p4: IntBuffer, p5: IntBuffer, p6: ByteBuffer) -> int: ...
    @overload
    @staticmethod
    def glGetDebugMessageLogKHR(p0: int, p1: int, p2: Any, p3: int, p4: Any, p5: int, p6: Any, p7: int, p8: Any, p9: int, p10: Any, p11: int, p12: Any, p13: int) -> int: ...
    @overload
    @staticmethod
    def glGetDebugMessageLogKHR(p0: int, p1: Any, p2: int, p3: Any, p4: int, p5: Any, p6: int, p7: Any, p8: int) -> Any: ...
    @staticmethod
    def glGetObjectLabelKHR(p0: int, p1: int) -> str: ...
    @staticmethod
    def glGetObjectPtrLabelKHR(p0: int) -> str: ...
    @overload
    @staticmethod
    def glGetSamplerParameterIivEXT(p0: int, p1: int, p2: Any, p3: int) -> None: ...
    @overload
    @staticmethod
    def glGetSamplerParameterIivEXT(p0: int, p1: int, p2: IntBuffer) -> None: ...
    @overload
    @staticmethod
    def glGetSamplerParameterIuivEXT(p0: int, p1: int, p2: IntBuffer) -> None: ...
    @overload
    @staticmethod
    def glGetSamplerParameterIuivEXT(p0: int, p1: int, p2: Any, p3: int) -> None: ...
    @overload
    @staticmethod
    def glGetTexParameterIivEXT(p0: int, p1: int, p2: IntBuffer) -> None: ...
    @overload
    @staticmethod
    def glGetTexParameterIivEXT(p0: int, p1: int, p2: Any, p3: int) -> None: ...
    @overload
    @staticmethod
    def glGetTexParameterIuivEXT(p0: int, p1: int, p2: Any, p3: int) -> None: ...
    @overload
    @staticmethod
    def glGetTexParameterIuivEXT(p0: int, p1: int, p2: IntBuffer) -> None: ...
    @staticmethod
    def glIsEnablediEXT(p0: int, p1: int) -> bool: ...
    @staticmethod
    def glMinSampleShadingOES(p0: float) -> None: ...
    @staticmethod
    def glObjectLabelKHR(p0: int, p1: int, p2: int, p3: str) -> None: ...
    @staticmethod
    def glObjectPtrLabelKHR(p0: int, p1: str) -> None: ...
    @staticmethod
    def glPatchParameteriEXT(p0: int, p1: int) -> None: ...
    @staticmethod
    def glPopDebugGroupKHR() -> None: ...
    @staticmethod
    def glPrimitiveBoundingBoxEXT(p0: float, p1: float, p2: float, p3: float, p4: float, p5: float, p6: float, p7: float) -> None: ...
    @staticmethod
    def glPushDebugGroupKHR(p0: int, p1: int, p2: int, p3: str) -> None: ...
    @overload
    @staticmethod
    def glSamplerParameterIivEXT(p0: int, p1: int, p2: Any, p3: int) -> None: ...
    @overload
    @staticmethod
    def glSamplerParameterIivEXT(p0: int, p1: int, p2: IntBuffer) -> None: ...
    @overload
    @staticmethod
    def glSamplerParameterIuivEXT(p0: int, p1: int, p2: IntBuffer) -> None: ...
    @overload
    @staticmethod
    def glSamplerParameterIuivEXT(p0: int, p1: int, p2: Any, p3: int) -> None: ...
    @staticmethod
    def glTexBufferEXT(p0: int, p1: int, p2: int) -> None: ...
    @staticmethod
    def glTexBufferRangeEXT(p0: int, p1: int, p2: int, p3: int, p4: int) -> None: ...
    @overload
    @staticmethod
    def glTexParameterIivEXT(p0: int, p1: int, p2: Any, p3: int) -> None: ...
    @overload
    @staticmethod
    def glTexParameterIivEXT(p0: int, p1: int, p2: IntBuffer) -> None: ...
    @overload
    @staticmethod
    def glTexParameterIuivEXT(p0: int, p1: int, p2: Any, p3: int) -> None: ...
    @overload
    @staticmethod
    def glTexParameterIuivEXT(p0: int, p1: int, p2: IntBuffer) -> None: ...
    @staticmethod
    def glTexStorage3DMultisampleOES(p0: int, p1: int, p2: int, p3: int, p4: int, p5: int, p6: bool) -> None: ...

    class DebugProcKHR:
        def onMessage(self, p0: int, p1: int, p2: int, p3: int, p4: str) -> None: ...
