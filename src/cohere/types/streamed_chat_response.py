# This file was auto-generated by Fern from our API Definition.

from __future__ import annotations

import typing

from .chat_citation_generation_event import ChatCitationGenerationEvent
from .chat_search_queries_generation_event import ChatSearchQueriesGenerationEvent
from .chat_search_results_event import ChatSearchResultsEvent
from .chat_stream_end_event import ChatStreamEndEvent
from .chat_stream_start_event import ChatStreamStartEvent
from .chat_text_generation_event import ChatTextGenerationEvent
from .chat_tool_calls_generation_event import ChatToolCallsGenerationEvent


class StreamedChatResponse_StreamStart(ChatStreamStartEvent):
    event_type: typing.Literal["stream-start"]

    class Config:
        frozen = True
        smart_union = True
        allow_population_by_field_name = True
        populate_by_name = True


class StreamedChatResponse_SearchQueriesGeneration(ChatSearchQueriesGenerationEvent):
    event_type: typing.Literal["search-queries-generation"]

    class Config:
        frozen = True
        smart_union = True
        allow_population_by_field_name = True
        populate_by_name = True


class StreamedChatResponse_SearchResults(ChatSearchResultsEvent):
    event_type: typing.Literal["search-results"]

    class Config:
        frozen = True
        smart_union = True
        allow_population_by_field_name = True
        populate_by_name = True


class StreamedChatResponse_TextGeneration(ChatTextGenerationEvent):
    event_type: typing.Literal["text-generation"]

    class Config:
        frozen = True
        smart_union = True
        allow_population_by_field_name = True
        populate_by_name = True


class StreamedChatResponse_CitationGeneration(ChatCitationGenerationEvent):
    event_type: typing.Literal["citation-generation"]

    class Config:
        frozen = True
        smart_union = True
        allow_population_by_field_name = True
        populate_by_name = True


class StreamedChatResponse_ToolCallsGeneration(ChatToolCallsGenerationEvent):
    event_type: typing.Literal["tool-calls-generation"]

    class Config:
        frozen = True
        smart_union = True
        allow_population_by_field_name = True
        populate_by_name = True


class StreamedChatResponse_StreamEnd(ChatStreamEndEvent):
    event_type: typing.Literal["stream-end"]

    class Config:
        frozen = True
        smart_union = True
        allow_population_by_field_name = True
        populate_by_name = True


StreamedChatResponse = typing.Union[
    StreamedChatResponse_StreamStart,
    StreamedChatResponse_SearchQueriesGeneration,
    StreamedChatResponse_SearchResults,
    StreamedChatResponse_TextGeneration,
    StreamedChatResponse_CitationGeneration,
    StreamedChatResponse_ToolCallsGeneration,
    StreamedChatResponse_StreamEnd,
]
