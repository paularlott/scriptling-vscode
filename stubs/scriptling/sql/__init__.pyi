"""
SQL plugin — MySQL, MariaDB and PostgreSQL client.

The DSN scheme picks the driver: ``postgres://`` (or ``postgresql://``),
``mysql://``, ``mariadb://`` (MySQL and MariaDB share the MySQL protocol).
The query/execute/close surface is identical to scriptling.sqlite; ``?``
placeholders become ``$n`` on PostgreSQL, which also accepts explicit
``$n``.
"""

from typing import Any, Dict, List, Optional, TypedDict


class ExecResult(TypedDict):
    """Result of Connection.execute(). last_insert_id is 0 on postgres."""

    last_insert_id: int
    rows_affected: int


_Row = Dict[str, Any]


class Connection:
    """A handle to an open database connection."""

    def query(self, sql: str, *params: Any) -> List[_Row]:
        """Execute a SELECT-style statement.

        Returns every row as a dict keyed by column name. Values are ints,
        floats, bools, strings, or None.
        """
        ...

    def query_iter(self, sql: str, *params: Any) -> Cursor:
        """Run a query and stream rows via a Cursor instead of a list."""
        ...

    def execute(self, sql: str, *params: Any) -> ExecResult:
        """Execute a statement that changes rows (INSERT/UPDATE/DELETE/DDL).

        Returns ``{"last_insert_id": int, "rows_affected": int}``.
        """
        ...


    def get_orm(self) -> ORM:
        """Return the ORM bound to this connection.

        query builders (select/update/delete -> .where(...)....
        fetch()/execute()), the quick insert form, criteria constructors
        (eq/any_of/...) and model gateways (table(factory, ...)).
        """
        ...

    def close(self) -> None:
        """Close the connection."""
        ...


class ORM:
    """Table helper from Connection.get_orm(): query builders, quick forms, models."""

    # quick forms

    def insert(self, table: str, values: Dict[str, Any], pk: str = "id") -> ExecResult:
        """Insert one row from a dict of column to value.

        last_insert_id works on every backend (RETURNING on postgres,
        through the primary key named by pk).
        """
        ...

    def tables(self) -> List[str]:
        """User table names in the current database, sorted."""
        ...

    def create_table(self, table: str) -> "TableBuilder":
        """Start a CREATE TABLE builder; .execute() runs the DDL."""
        ...

    def drop_table(self, table: str) -> ExecResult:
        """DROP TABLE IF EXISTS."""
        ...

    # query builders

    def select(self, table: str, *columns: str) -> "QueryBuilder":
        """Start a chained query; .fetch() runs it. Columns optional (all)."""
        ...

    def update(self, table: str, values: Dict[str, Any]) -> "UpdateQuery":
        """Start a chained update; .where(...) then .execute(). Where required."""
        ...

    def delete(self, table: str) -> "DeleteQuery":
        """Start a chained delete; .where(...) then .execute(). Where required."""
        ...

    # criteria

    def eq(self, column: str, value: Any) -> "Criterion": ...
    def ne(self, column: str, value: Any) -> "Criterion": ...
    def lt(self, column: str, value: Any) -> "Criterion": ...
    def le(self, column: str, value: Any) -> "Criterion": ...
    def gt(self, column: str, value: Any) -> "Criterion": ...
    def ge(self, column: str, value: Any) -> "Criterion": ...
    def like(self, column: str, pattern: str) -> "Criterion": ...
    def ilike(self, column: str, pattern: str) -> "Criterion": ...
    def one_of(self, column: str, values: List[Any]) -> "Criterion": ...
    def not_one_of(self, column: str, values: List[Any]) -> "Criterion": ...
    def is_null(self, column: str) -> "Criterion": ...
    def not_null(self, column: str) -> "Criterion": ...
    def any_of(self, *criteria: "Criterion") -> "Criterion": ...
    def all_of(self, *criteria: "Criterion") -> "Criterion": ...

    # models

    def table(self, factory: Any, table: str, pk: str = "id",
              columns: Optional[List[str]] = ...) -> "ModelGateway":
        """Bind a row factory to a table.

        Without columns the gateway writes every column the table has
        (read from the schema once per get_orm() and cached); pass a list
        to manage a subset.
        """
        ...


class TableBuilder:
    """A CREATE TABLE builder from orm.create_table(); every method returns the builder."""

    def column(self, name: str, col_type: str, primary_key: bool = False,
               autoincrement: bool = False, nullable: bool = True,
               unique: bool = False, default: Any = ...) -> "TableBuilder":
        """Add a column; col_type is raw SQL ("text", "varchar(100)", ...)."""
        ...

    def if_not_exists(self) -> "TableBuilder": ...
    def execute(self) -> ExecResult: ...


class Cursor:
    """Row stream from Connection.query_iter()."""

    def next(self) -> Optional[Dict[str, Any]]:
        """The next row as a dict, or None when exhausted."""
        ...

    def close(self) -> None: ...


class RowIterator:
    """Row stream from QueryBuilder.iterate(); supports for-in."""

    def __iter__(self) -> "RowIterator": ...
    def __next__(self) -> Dict[str, Any]: ...
    def close(self) -> None: ...


class Criterion:
    """A composable condition from the orm.eq()/any_of()/... constructors."""

    def _sql(self, ctx: Dict[str, Any]) -> List[Any]: ...


class QueryBuilder:
    """A chained query from orm.select(); every method returns the query."""

    def where(self, column: str, op: str, value: Any) -> "QueryBuilder":
        """Add an AND condition; op in = != <> < <= > >= like."""
        ...

    def where(self, criterion: Criterion) -> "QueryBuilder":
        """Add an AND condition from orm.eq()/any_of()/... ."""
        ...

    def where_sql(self, fragment: str, *params: Any) -> "QueryBuilder":
        """Escape hatch: raw SQL fragment with ? placeholders."""
        ...

    def order_by(self, column: str, desc: bool = False) -> "QueryBuilder": ...
    def limit(self, n: int) -> "QueryBuilder": ...
    def offset(self, n: int) -> "QueryBuilder": ...
    def fetch(self) -> List[Dict[str, Any]]: ...
    def iterate(self) -> "RowIterator": ...
    def one(self) -> Optional[Dict[str, Any]]: ...
    def count(self) -> int: ...


class UpdateQuery:
    """A chained update from orm.update(table, values); every method returns the query."""

    def where(self, column: str, op: str, value: Any) -> "UpdateQuery":
        """Add an AND condition; op in = != <> < <= > >= like."""
        ...

    def where(self, criterion: Criterion) -> "UpdateQuery":
        """Add an AND condition from orm.eq()/any_of()/... ."""
        ...

    def where_sql(self, fragment: str, *params: Any) -> "UpdateQuery":
        """Escape hatch: raw SQL fragment with ? placeholders."""
        ...

    def execute(self) -> ExecResult:
        """Run the update. Refuses to run without a where clause."""
        ...


class DeleteQuery:
    """A chained delete from orm.delete(table); every method returns the query."""

    def where(self, column: str, op: str, value: Any) -> "DeleteQuery":
        """Add an AND condition; op in = != <> < <= > >= like."""
        ...

    def where(self, criterion: Criterion) -> "DeleteQuery":
        """Add an AND condition from orm.eq()/any_of()/... ."""
        ...

    def where_sql(self, fragment: str, *params: Any) -> "DeleteQuery":
        """Escape hatch: raw SQL fragment with ? placeholders."""
        ...

    def execute(self) -> ExecResult:
        """Run the delete. Refuses to run without a where clause."""
        ...


class ModelGateway:
    """Row-object mapping from orm.table(factory, table, ...)."""

    def get(self, pk_value: Any) -> Any:
        """Factory(row) for the primary key, or None."""
        ...

    def insert(self, obj: Any) -> ExecResult: ...
    def save(self, obj: Any) -> ExecResult:
        """Update by primary key."""
        ...

    def delete(self, target: Any) -> ExecResult:
        """Delete by instance (pk field) or raw primary key."""
        ...

    def count(self) -> int: ...
    def select(self, *columns: str) -> QueryBuilder: ...


def connect(dsn: str) -> Connection:
    """Connect to a relational database server.

    Parameters:
        dsn: e.g. ``"postgres://user:pass@host:5432/db"``,
            ``"mysql://user:pass@host:3306/db"``,
            ``"mariadb://user:pass@host:3306/db"``. The server address must
            pass the host's network policy.
    """
    ...
